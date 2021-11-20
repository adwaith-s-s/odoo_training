from odoo import api, fields, models


class ProductWarrantyDetails(models.AbstractModel):
    _name = 'report.product_warranty.report_warranty_detail'
    _description = 'Warranty Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print('nothing', data.get('form_data').get('start_date'), '-----', docids)

        product_ids = (str(data.get('form_data').get('product_ids')))
        product_ids = product_ids.lstrip("[").rstrip("]")
        print(product_ids)

        query = 'SELECT * FROM public.product_warranty_warranty'
        if data.get('form_data').get('partner_id') or data.get('form_data').get('product_ids')\
                or data.get('form_data').get('start_date') or data.get('form_data').get('end_date'):
            query += '\nWHERE'

        if data.get('form_data').get('partner_id'):
            query += '\npartner_id ='+str(data.get('form_data').get('partner_id')[0])
        if data.get('form_data').get('partner_id') and (
                data.get('form_data').get('product_ids') or data.get('form_data').get('start_date') or data.get(
                'form_data').get('end_date')):
            query += '\nAND'

        if data.get('form_data').get('product_ids'):
            query += '\nproduct_id in (' + product_ids + ')'
        if data.get('form_data').get('product_ids') and (
                data.get('form_data').get('start_date') or data.get('form_data').get('end_date')):
            query += '\nAND'

        if data.get('form_data').get('start_date'):
            query += '\ncreate_date > \''+str(data.get('form_data').get('start_date'))+'\''
        if data.get('form_data').get('start_date') and data.get('form_data').get('end_date'):
            query += '\nAND'

        if data.get('form_data').get('end_date'):
            query += '\ncreate_date < \''+str(data.get('form_data').get('end_date'))+'\''

        query += '\nORDER BY id ASC'

        self.env.cr.execute(query)
        docs = self.env.cr.fetchall()
        print(docs)
        # docs = self.env['product.warranty.warranty'].search([])
        return {
            'docs': docs
        }
