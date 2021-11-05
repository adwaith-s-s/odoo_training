from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    project_created = fields.Boolean(default=False)

    def action_create_project(self):
        self.project_created = True
        self.order_line.project_created = True
        project = self.env['project.project'].create({
            'name': self.name,
            'label_tasks': 'Sale Order',
            'user_id': self.user_id.id,
            'partner_id': self.partner_id.id,
            'privacy_visibility': 'portal',
            'company_id': self.company_id.id,
            'sale_order_id': self.id,
        })
        milestone = []
        for record in self.order_line:
            if record.mile_stone not in milestone:
                milestone.append(record.mile_stone)
                parent_task = self.env['project.task'].create({
                    'project_id': project.id,
                    'name': 'Milestone'+'-'+str(record.mile_stone)
                })
                for rec in self.order_line:
                    if rec.mile_stone == record.mile_stone:
                        self.env['project.task'].create({
                            'project_id': project.id,
                            'name': str(record.product_id.name) + '/MS-' + str(record.mile_stone),
                            'parent_id': parent_task.id
                        })


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    mile_stone = fields.Integer(string='Mile Stone Task')
    project_created = fields.Boolean(default=False)



