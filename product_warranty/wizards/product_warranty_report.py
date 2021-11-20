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
        # domain = []
        product_ids_list =[]
        for products in self.product_ids:
            product_ids_list.append(products.id)
        product_ids_private = str(product_ids_list)
        product_ids_private = product_ids_private.lstrip("[").rstrip("]")
        print(product_ids_private)

        query = 'SELECT * FROM public.product_warranty_warranty'
        if self.partner_id or self.product_ids or self.start_date or self.end_date:
            query += '\nWHERE'

        if self.partner_id:
            query += '\npartner_id =' + str(self.partner_id)
        if self.partner_id and (self.product_ids or self.start_date or self.end_date):
            query += '\nAND'

        if self.product_ids:
            query += '\nproduct_id in (' + product_ids_private + ')'
        if self.product_ids and (self.start_date or self.end_date):
            query += '\nAND'

        if self.start_date:
            query += '\ncreate_date > \'' + str(self.start_date) + '\''
        if self.start_date and self.end_date:
            query += '\nAND'

        if self.end_date:
            query += '\ncreate_date < \'' + str(self.end_date) + '\''

        query += '\nORDER BY id ASC'

        self.env.cr.execute(query)
        docs = self.env.cr.fetchall()

        # warranties = self.env['product.warranty.warranty'].search_read(domain)
        data = {
            'warranties': docs,
            'form_data': self.read()[0]
        }
        return self.env.ref('product_warranty.action_report_product_warranty_xlsx').report_action(self, data=data)

    def action_print_report(self):
        data = {
            'form_data': self.read()[0],
        }
        return self.env.ref('product_warranty.action_report_product_warranty').report_action(self, data=data)

