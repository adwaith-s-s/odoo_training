import base64
import io
from odoo import models


class ProductWarrantyXlsxReport(models.AbstractModel):
    _name = 'report.product_warranty.report_warranty_detail_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, warranties):
        print("Excel report loading", data['warranties'])
        sheet = workbook.add_worksheet('warranties')
        bold = workbook.add_format({'bold': True})

        row = 3
        col = 3
        sheet.write(row, col, 'Reference', bold)
        sheet.write(row, col+1, 'Invoice', bold)
        sheet.write(row, col+2, 'Product', bold)


