from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        print("send confirm email")
        print(self.access_url)
        self.env.ref('invoice_payment_link.email_invoice_payment').send_mail(self.id, force_send=True)
        self._post(soft=False)
        return False
