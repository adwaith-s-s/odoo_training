# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Milestone Tasks',
    'version': '14.0.1.0.0',
    'summary': 'Mile stone tasks to sale order line',
    'sequence': 10,
    'description': """Add Milestone Tasks to Sale order lines""",
    'category': 'Sales/Sales',
    'website': 'https://www.odoodemo.com',
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/sale_views.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
