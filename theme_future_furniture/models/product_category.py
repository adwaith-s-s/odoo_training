

from odoo import models, fields


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    category_count = fields.Integer("Count", compute="_compute_category_count")

    def _compute_category_count(self):
        for ct in self:
            product_ids = self.env['product.template'].search(
                [('website_published', '=', True)])
            count = 0
            for rec in product_ids:
                for cat in rec.public_categ_ids:
                    if cat in ct:
                        count += 1
            ct.category_count = count


class Product(models.Model):
    _inherit = 'product.template'

    views = fields.Integer('Views')
    most_viewed = fields.Boolean('Most Viewed')
