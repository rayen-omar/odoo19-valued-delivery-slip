# -*- coding: utf-8 -*-
{
    'name': 'Valued Delivery Slip',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Add unit price, discount, tax and totals to the Delivery Slip report',
    'description': """
<p>A clean, light, and robust module that adds pricing, discount, and tax
details to the standard Delivery Slip (Bon de Livraison) report.</p>

<p>By default, Odoo's Delivery Slip only displays product quantities
(ordered and delivered). This module inherits the standard report to
display complete financial information when the delivery is linked to
a Sales Order.</p>

<h3>Features</h3>
<ul>
<li>Unit Price, Discount %, Taxes and Amount columns added to the delivery lines</li>
<li>Financial totals summary: Untaxed Amount, Tax breakdown, Total</li>
<li>Conditional visibility: financial data only shows when the delivery
is linked to a Sales Order; internal transfers keep the standard,
non-valued layout</li>
<li>Pure QWeb inheritance: no Python overrides, no database changes</li>
</ul>

<h3>Support</h3>
<p>Website: <a href="https://www.benamor.tech/">https://www.benamor.tech/</a><br/>
WhatsApp: +216 95 129 848</p>
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