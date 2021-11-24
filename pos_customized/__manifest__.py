# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Customized',
    'version': '14.0.1.0.0',
    'summary': 'My POS Customizations',
    'sequence': 10,
    'description': """Module to add my customizations to Point of Sale""",
    'category': 'Point of Sale',
    'website': 'https://www.odoodemo.com',
    'depends': [
        'base',
        'point_of_sale',
        'product',
        'resource'
    ],
    'data': [
        'views/product.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'qweb': ['static/src/xml/pos.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
