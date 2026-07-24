====================
Valued Delivery Slip
====================

.. image:: https://img.shields.io/badge/maturity-Production%2FStable-green.png
    :target: https://github.com/rayen-omar/odoo19-valued-delivery-slip
    :alt: Production/Stable
.. image:: https://img.shields.io/badge/licence-LGPL--3-blue.png
    :target: https://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3

This Odoo 19 module adds financial details directly to your PDF Delivery Slip (stock.picking). It displays unit prices, discounts, taxes, and amounts, as well as a complete financial summary (untaxed amount, taxes, and total) if the delivery is linked to a confirmed Sales Order.

.. contents:: :local:

Features
========

* Adds financial columns to the Delivery Slip PDF report (Unit Price, Discount %, Taxes, Amount).
* Includes a financial summary section (Untaxed Amount, Taxes breakdown, Total).
* Dynamically adapts to show these financial values only if the delivery is linked to a confirmed Sales Order; otherwise, the standard quantities-only layout is retained.
* 100% QWeb (XML) implementation with no database alterations and no custom Python code.

Configuration
=============

No configuration is required for this module. Once installed, it automatically updates the standard delivery slip report layout.

Usage
=====

To use this module:

1. Go to the **Sales** app and create a new Sales Order (SO).
2. Add lines with products, unit prices, discounts, and taxes, then **Confirm** the Sales Order.
3. Open the linked **Delivery** transfer generated under the Sales Order.
4. Click on **Print** > **Delivery Slip**. The PDF report will contain the detailed pricing columns and financial summary.
5. If you print a Delivery Slip that is not linked to any confirmed Sales Order, it will automatically fall back to the standard layout (quantities only).

Screenshots
===========

**Before** — Standard Odoo Delivery Slip (quantities only):

.. image:: https://raw.githubusercontent.com/rayen-omar/odoo19-valued-delivery-slip/19.0/valued_delivery_slip/static/description/bl_before.png
   :alt: Delivery Slip before

**After** — With Valued Delivery Slip installed (pricing, discount, tax, totals):

.. image:: https://raw.githubusercontent.com/rayen-omar/odoo19-valued-delivery-slip/19.0/valued_delivery_slip/static/description/bl_after.png
   :alt: Delivery Slip after

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/rayen-omar/odoo19-valued-delivery-slip/issues>`_.
In case of trouble, please check there if your issue has already been reported. If you spotted it first, help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Authors
-------

* BenAmor Rayeen <benomorr326@gmail.com> (https://www.benamor.tech/)

Contributors
------------

* BenAmor Rayeen <benomorr326@gmail.com>

Maintainers
-----------

This module is maintained by BenAmor Rayeen.
