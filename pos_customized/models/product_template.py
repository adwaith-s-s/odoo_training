from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_owner = fields.Many2one('res.partner', string="Product Owner")
    rating = fields.Selection(selection=[
            ('1', '1 Star'),
            ('2', '2 Star'),
            ('3', '3 Star'),
            ('4', '4 Star'),
            ('5', '5 Star'),
        ], string='Rating', default='3')
