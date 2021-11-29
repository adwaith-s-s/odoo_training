# -*- coding: utf-8 -*-


from odoo import http
from odoo.http import request


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
                duration = post.get('duration')
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
