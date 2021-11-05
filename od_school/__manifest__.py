# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'School Management',
    'version': '14.0.1.0.0',
    'summary': 'School Management Module',
    'sequence': 1000,
    'description': """School Management Module""",
    'category': 'Human Resources',
    'website': 'https://www.odoodemo.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/students.xml',
        'views/teachers.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
