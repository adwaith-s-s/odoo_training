from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'project.project'

    sale_order_id = fields.Many2one('sale.order', string="Sale order project")
