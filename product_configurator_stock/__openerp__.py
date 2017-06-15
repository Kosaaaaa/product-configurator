# -*- coding: utf-8 -*-
{
    'name': 'Product Configurator for Stock',
    'version': '9.0.1.0.0',
    'category': 'Generic Modules/Stock',
    'summary': 'Product configuration interface module for Stock',
    'author': 'Pledra',
    'license': 'AGPL-3',
    'website': 'http://www.pledra.com/',
    # TODO: Enable loading mrp module before lot and remove direct dependency
    'depends': ['stock', 'product_configurator_mrp'],
    "data": [
        'views/stock_lot_view.xml',
        'views/assets.xml'
    ],
    'demo': [
        'demo/product_template.xml'
    ],
    'images': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
