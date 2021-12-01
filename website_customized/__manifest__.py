# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Website Customized',
    'version': '14.0.1.0.0',
    'summary': 'My Website Customizations',
    'sequence': 10,
    'description': """Module to add my customizations to Website""",
    'category': 'Website/Website',
    'website': 'https://www.odoodemo.com',
    'depends': [
        'base',
        'website',
        'sale',
        'product',
    ],
    'data': [
        'data/menu.xml',
        'views/templates.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
