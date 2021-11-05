from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    warranty_ids = fields.One2many('product.warranty.warranty', 'invoice_id', string="Warranty")
