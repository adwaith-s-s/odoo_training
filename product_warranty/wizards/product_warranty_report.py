# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductWarrantyReportWizard(models.TransientModel):
    _name = "product.warranty.report.wizard"
    _description = "Print Warranty Wizard"

    partner_id = fields.Many2one('res.partner', string="Customer")
    product_ids = fields.Many2many('product.product', string="Products", ondelete='cascade')

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    def action_print_report(self):
        warranties = self.env['product.warranty.warranty'].search_read([])
        data = {
            'form': self.read()[0],
            'warranties': warranties
        }
        return self.env.ref('product_warranty.action_report_product_warranty').report_action(self, data=data)
