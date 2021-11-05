from odoo import api, fields, models


class WarrantyStockMove(models.Model):
    _inherit = 'stock.move'

    warranty_id = fields.Many2one('product.warranty.warranty', string='Warranty', index=True)
