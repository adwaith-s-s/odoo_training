# -*- coding: utf-8 -*-

from odoo import models,fields, api, _


class FutureFurnitureConfiguration(models.Model):
    _name = 'future_furniture.configuration'

    name = fields.Char('Name')
    featured_product_ids = fields.Many2many('product.product')


class Product(models.Model):
    _inherit = 'product.template'

    qty_sold = fields.Integer('Quantity sold')
    views = fields.Integer('Views')
    top_selling = fields.Boolean('TopSelling')
    most_viewed = fields.Boolean('Most Viewed')
