import base64
import io
from odoo import models


class ProductWarrantyXlsxReport(models.AbstractModel):
    _name = 'report.product_warranty.report_warranty_detail_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, warranties):
        sheet = workbook.add_worksheet('Warranty Requests')
        sheet.set_column('A:A', 15)
        sheet.set_column('B:B', 20)
        sheet.set_column('C:C', 35)
        bold = workbook.add_format({'bold': True})

        print(data['warranties'])

        row = 0
        col = 0

        sheet.write(row, col, 'Reference', bold)
        sheet.write(row, col+1, 'Invoice', bold)
        sheet.write(row, col+2, 'Product', bold)

        for warranties in data['warranties']:
            row += 1
            sheet.write(row, col, warranties[7])
            sheet.write(row, col + 1, warranties[1])
            sheet.write(row, col + 2, warranties[11])





