from odoo import api, fields, models


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"
    product_owner = fields.Many2one(related='product_id.product_tmpl_id.product_owner',
                           string='Product Owner', store=True)
