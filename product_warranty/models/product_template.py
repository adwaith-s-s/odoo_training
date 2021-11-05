from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    has_warranty = fields.Boolean('Has Warranty', default=True)
    warranty_no_of_days = fields.Integer('Warranty Period (days)', default='120')
    warranty_type = fields.Selection([
        ('service_warranty', 'Service Warranty'),
        ('replacement_warranty', 'Replacement warranty'),
    ], default='service_warranty')
