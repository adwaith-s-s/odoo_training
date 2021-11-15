# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Product Warranty',
    'version': '14.0.4.0.0',
    'summary': 'Product Warranty Module',
    'sequence': 10,
    'description': """Product Warranty Module""",
    'category': 'Sales/Sales',
    'website': 'https://www.odoodemo.com',
    'depends': [
        'base',
        'account',
        'resource',
        'product',
        'stock',
        'mail',
        'web_domain_field',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/product_warranty_report_view.xml',
        'views/warranty.xml',
        'views/product.xml',
        'views/invoice_form_view.xml',
        'report/report.xml',
        'report/warranty_details_template.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
