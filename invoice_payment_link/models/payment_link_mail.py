import hmac
import hashlib

from odoo import api, fields, models
from werkzeug import urls


class AccountMove(models.Model):
    _inherit = 'account.move'

    link = fields.Char(string='Payment Link', compute='_compute_values')
    access_token = fields.Char(compute='_compute_values')

    @api.depends('amount_total', 'name', 'partner_id', 'currency_id')
    def _compute_values(self):
        secret = self.env['ir.config_parameter'].sudo().get_param('database.secret')
        for payment_link in self:
            token_str = '%s%s%s' % (payment_link.partner_id.id, payment_link.amount_total, payment_link.currency_id.id)
            payment_link.access_token = hmac.new(secret.encode('utf-8'), token_str.encode('utf-8'),
                                                 hashlib.sha256).hexdigest()
        # must be called after token generation, obvsly - the link needs an up-to-date token
        self._generate_link()

    def _generate_link(self):
        for payment_link in self:
            link = ('%s/website_payment/pay?reference=%s&amount=%s&currency_id=%s'
                    '&partner_id=%s&access_token=%s') % (
                        self.get_base_url(),
                        urls.url_quote_plus(payment_link.name),
                        payment_link.amount_total,
                        payment_link.currency_id.id,
                        payment_link.partner_id.id,
                        payment_link.access_token
                    )
            if payment_link.company_id:
                link += '&company_id=%s' % payment_link.company_id.id
            link += '&invoice_id=%s' % payment_link.id
            payment_link.link = link

    def action_post(self):
        print("send confirm email")
        print(self.link)
        res = super(AccountMove, self).action_post()
        self.env.ref('invoice_payment_link.email_invoice_payment').send_mail(self.id, force_send=True)
        return res
