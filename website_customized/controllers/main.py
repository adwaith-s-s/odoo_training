# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers.web import Home

from odoo import http
from odoo.http import request
import base64


class Main(http.Controller):
    @http.route('/maintenance_request', type='http', auth="user", website=True)
    def web_maintenance_request(self, **post):

        if post.get('name'):
            name = post.get('name')

            if post.get('maintenance_team_id'):
                maintenance_team_id = int(post.get('maintenance_team_id'))
                equipment_id = int(post.get('equipment_id'))
                maintenance_type = post.get('maintenance_type')
                user_id = int(post.get('user_id'))
                schedule_date = post.get('schedule_date')
                duration = float(post.get('duration'))
                print(duration)
                priority = post.get('priority')
                description = post.get('description')
                request.env['maintenance.request'].sudo().create({
                    'name': name,
                    'maintenance_team_id': maintenance_team_id,
                    'equipment_id': equipment_id,
                    'maintenance_type': maintenance_type,
                    'user_id': user_id,
                    'schedule_date': schedule_date,
                    'duration': duration,
                    'priority': priority,
                    'description': description
                })
                return request.redirect('/maintenance_request?submitted=1')

        return request.render('website_customized.web_maintenance_request_form', {
            'maintenance_teams': request.env['maintenance.team'].search([]),
            'equipments': request.env['maintenance.equipment'].search([]),
            'users': request.env['res.users'].search([]),
            'submitted': post.get('submitted', False)
        })


class WebsiteHomeCustomized(Home):
    @http.route()
    def index(self, **kw):

        current_website = request.website
        super(WebsiteHomeCustomized, self).index()

        product_records_sold = {}
        sorted_product_records_sold = []
        sales = request.env['sale.order'].search(
            [('website_id', '=', current_website.id), ('state', 'in', ('sale', 'done'))])
        for s in sales:
            orders = request.env['sale.order.line'].search([('order_id', '=', s.id)])
            for order in orders:
                if order.product_id:
                    if order.product_id not in product_records_sold:
                        product_records_sold.update({order.product_id: 0})
                    product_records_sold[order.product_id] += order.product_uom_qty

        for product_id, quantity in sorted(product_records_sold.items(), key=lambda kv: kv[1], reverse=True)[:6]:
            sorted_product_records_sold.append(
                {'product': product_id.image_512, 'id': product_id.product_tmpl_id.id,
                 'name': product_id.product_tmpl_id.name, 'qty': int(quantity)})

        product_records_view = {}
        sorted_product_records_view = []
        visit = request.env['website.track'].search([])
        for v in visit:
            if v.product_id:
                product_records_view.update({v.product_id: 0})
                for x in visit:
                    if v.product_id == x.product_id:
                        product_records_view[v.product_id] += 1

        for product_id, views in sorted(product_records_view.items(), key=lambda kv: kv[1], reverse=True)[:6]:
            sorted_product_records_view.append(
                {'product': product_id.image_512, 'id': product_id.product_tmpl_id.id,
                 'name': product_id.product_tmpl_id.name, 'views': views})

        return request.render('website.homepage', {
            'most_sold_products': sorted_product_records_sold,
            'most_viewed_products': sorted_product_records_view
        })


