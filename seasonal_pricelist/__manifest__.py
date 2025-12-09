{
    'name': 'Seasonal PriceList',
    'version': '1.0',
    'category': 'Extra Tools',
    'description': 'Seasonal Pricelist',
    'sequence': 100,
    'summary': 'Seasonal Pricelist',
    'author': 'Vashmitha',
    'license': 'LGPL-3',
    'website': '',
    'depends': ['sale', 'stock', 'product'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}