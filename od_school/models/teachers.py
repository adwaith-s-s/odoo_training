from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = "school.teachers"
    _description = "School Teachers Information"

    name = fields.Char(string='Name', required=True)
    department = fields.Char(string='Department')
    salary = fields.Integer(string='Salary')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=False, default='male')
    note = fields.Text(string='Description')