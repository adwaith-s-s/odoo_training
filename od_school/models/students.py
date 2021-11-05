from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student Information"

    name = fields.Char(string='Name', required=True)
    course = fields.Char(string='Course')
    department = fields.Char(string='Department')
    year = fields.Selection([
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
    ], required=True, default='1')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')