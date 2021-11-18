# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductWarrantyReportWizard(models.TransientModel):
    _name = "product.warranty.report.wizard"
    _description = "Print Warranty Wizard"

    partner_id = fields.Many2one('res.partner', string="Customer")
    product_ids = fields.Many2many('product.product', string="Products", ondelete='cascade')

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    def action_print_excel_report(self):
        domain = []
        warranties = self.env['product.warranty.warranty'].search_read()
        data = {
            'warranties': warranties,
            'form_data': self.read()[0]
        }
        return self.env.ref('product_warranty.action_report_product_warranty_xlsx').report_action(self, data=data)

    def action_print_report(self):
        domain = []
        customer = self.partner_id
        if customer:
            domain += [('partner_id', '=', customer.id)]
        product_ids = []
        for rec in self.product_ids:
            product_ids.append(rec.id)
        if product_ids:
            domain += [('product_id', 'in', product_ids)]
        start_date = self.start_date
        if start_date:
            domain += [('create_date', '>=', start_date)]
        end_date = self.end_date
        if end_date:
            domain += [('create_date', '<=', end_date)]

        warranties = self.env['product.warranty.warranty'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'warranties': warranties,
        }
        return self.env.ref('product_warranty.action_report_product_warranty').report_action(self, data=data)


