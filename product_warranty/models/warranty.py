import json
import datetime


from odoo import api, fields, models


class ProductWarranty(models.Model):
    _name = "product.warranty.warranty"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Product Warranty"
    _order = "id desc"

    invoice_id = fields.Many2one('account.move', string='Invoice')
    partner_id = fields.Many2one('res.partner', string="Customer", related='invoice_id.partner_id')
    product_id = fields.Many2one('product.product', string="Product", ondelete='set null')
    product_id_domain = fields.Char(compute="_compute_product_id_domain", readonly=True, store=False,)

    lot_name = fields.Many2one('stock.production.lot', 'Lot/Serial Number')
    has_tracking = fields.Selection(related='product_id.tracking', string='Product with Tracking')

    inv_date = fields.Date(related='invoice_id.date', store=True, readonly=True, index=True, copy=False,
                           group_operator='min')
    expiry_date = fields.Date(store=True, readonly=True, index=True, copy=False, group_operator='min')
    sequence = fields.Integer(default=10)

    name = fields.Char(string="Warranty no", readonly=True, required=True, copy=False, default='New')

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('received', 'Received'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')

    def action_submit(self):
        self.state = 'to_approve'

    def action_approve(self):
        self.state = 'approved'

    def action_to_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def action_receive(self):
        self.state = 'received'

        customer_location = self.env.ref('stock.stock_location_customers')
        warranty_location = self.env.ref('product_warranty.product_warranty_location')

        move = self.env['stock.move'].create({
            'name': self.name,
            'location_id': customer_location.id,
            'location_dest_id': warranty_location.id,
            'product_id': self.product_id.id,
            'product_uom': self.product_id.uom_id.id,
            'product_uom_qty': 1.0,
            'warranty_id': self.id,
        })
        move._action_confirm()
        move._action_assign()
        move.move_line_ids.qty_done = 1.0
        move.move_line_ids.lot_id = self.lot_name
        move._action_done()

    def action_return(self):
        self.state = 'done'

        customer_location = self.env.ref('stock.stock_location_customers')

        if self.product_id.warranty_type == 'service_warranty':
            warranty_location = self.env.ref('product_warranty.product_warranty_location')
        elif self.product_id.warranty_type == 'replacement_warranty':
            warranty_location = self.env.ref('stock.stock_location_stock')

        move = self.env['stock.move'].create({
            'name': self.name,
            'location_id': warranty_location.id,
            'location_dest_id': customer_location.id,
            'product_id': self.product_id.id,
            'product_uom': self.product_id.uom_id.id,
            'product_uom_qty': 1.0,
            'warranty_id': self.id,
        })
        move._action_confirm()
        move._action_assign()
        move.move_line_ids.qty_done = 1.0
        move.move_line_ids.lot_id = self.lot_name
        move._action_done()

    @api.onchange('product_id')
    def warranty_expiry_calculation(self):
        if self.inv_date:
            self.expiry_date = self.inv_date + datetime.timedelta(days=self.product_id.warranty_no_of_days)
        self.has_tracking = self.product_id.tracking

    @api.depends('invoice_id')
    def _compute_product_id_domain(self):
        product_list = []
        for rec in self.invoice_id.invoice_line_ids.product_id:
            product_list.append(rec.id)
        self.product_id_domain = json.dumps([('id', 'in', product_list), ('type', '=', 'product'),
                                             ('has_warranty', '=', 'True')])

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'product.warranty') or 'New'
        result = super(ProductWarranty, self).create(vals)
        return result

    # @api.onchange('invoice_id')
    # def _product_id_domain(self):
    #     product_list = []
    #     for record in self.invoice_id.invoice_line_ids.product_id:
    #         product_list.append(record.id)
    #     return {'domain': {'product_id': [('id', 'in', product_list)]}}
