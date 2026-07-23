# -*- coding: utf-8 -*-
{
    'name': 'Valued Delivery Slip',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Add unit price, discount, tax and totals to the Delivery Slip report',
    'description': """
Valued Delivery Slip for Odoo 19 (Bon de Livraison Valorisé)
===============================================================

A clean, light, and robust module that adds pricing, discount, and tax
details to the standard Delivery Slip (Bon de Livraison) report.

By default, Odoo's Delivery Slip only displays product quantities
(ordered and delivered). This module inherits the standard report to
display complete financial information when the delivery is linked to
a Sales Order.

Features
--------
* Unit Price, Discount %, Taxes and Amount columns added to the delivery lines
* Financial totals summary: Untaxed Amount, Tax breakdown, Total
* Conditional visibility: financial data only shows when the delivery
  is linked to a Sales Order; internal transfers keep the standard,
  non-valued layout
* Pure QWeb inheritance: no Python overrides, no database changes

Support
-------
Website: https://www.benamor.tech/
WhatsApp: +216 95 129 848
    """,
    'author': 'BenAmor Rayeen',
    'website': 'https://www.benamor.tech/',
    'depends': ['base', 'stock', 'sale_stock'],
    'data': [
        'views/report_deliveryslip.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}