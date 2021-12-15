# -*- coding: utf-8 -*-
{
    'name': 'Theme Future Furniture',
    'description': 'Theme Future Furniture is an attractive and modern eCommerce Website theme',
    'summary': 'Theme Future Furniture is a new kind of Theme. '
               'The theme is a very user-friendly and is suitable for your eCommerce website with blog.',
    'category': 'Theme/website',
    'version': '14.0.1.0.0',
    'author': 'Demo',
    'company': 'Demo Company',
    'maintainer': 'Demo Company',
    'website': "https://www.demo.odoo",
    'depends': ['website', 'website_sale', 'website_blog', 'website_sale_wishlist', 'website_sale_comparison'],
    'data': [
        'views/header.xml',
        'views/assets.xml',
        'views/shop.xml',
        'views/shop_sidebar.xml',
        'views/cart.xml',
        'views/404.xml',
        'views/snippets/trending.xml'
    ],
    'images': [
    ],

    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
