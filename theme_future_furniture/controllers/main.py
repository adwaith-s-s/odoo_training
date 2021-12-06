from werkzeug.exceptions import NotFound
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import TableCompute, WebsiteSale
from odoo import http
from odoo.http import request
from odoo import fields
import datetime


class WebsiteProduct(http.Controller):

    @http.route('/get_trending_product', auth='public', type='json',
                website=True)
    def get_trending_product(self):
        products = request.env['product.template'].sudo().search([])
        for each in products:
            each.views = 0
            each.most_viewed = False
        date = fields.Datetime.now()
        date_before = date - datetime.timedelta(days=7)
        products = request.env['website.track'].sudo().search(
            [('visit_datetime', '<=', date),
             ('visit_datetime', '>=', date_before),
             ('product_id', '!=', False)])
        for pro in products:
            pro.product_id.views = pro.product_id.views + 1

        product_ids = request.env['product.template'].sudo().search(
            [('is_published', '=', True)],
            order='views desc', limit=4)

        print(product_ids)

        product_ids.most_viewed = True
        rating = request.website.viewref('website_sale.product_comment').active
        res = {'products': []}
        for product in product_ids:
            combination_info = product._get_combination_info()
            res_product = product.read(['id', 'name', 'website_url'])[0]
            res_product.update(combination_info)
            if rating:
                res_product['rating'] = request.env["ir.ui.view"]._render_template(
                    'portal_rating.rating_widget_stars_static', values={
                        'rating_avg': product.rating_avg,
                        'rating_count': product.rating_count,
                    })
            else:
                res_product['rating'] = 0
            res['products'].append(res_product)
        products = res['products']
        values = {'product_ids': products}
        response = http.Response(
            template='theme_future_furniture.trending_snippet', qcontext=values)
        return response.render()
