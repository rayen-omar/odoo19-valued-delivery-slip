# -*- coding: utf-8 -*-
{
    'name': 'Tahri Template BL',
    'version': '19.0.1.0.0',
    'category': 'Custom',
    'summary': 'Template module for Tahri BL customizations',
    'description': """
        This is a template/skeleton module for Tahri BL customizations,
        including displaying pricing and tax details on the Delivery Slip (BL).
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'stock', 'sale_stock'],
    'data': [
        'views/report_deliveryslip.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
