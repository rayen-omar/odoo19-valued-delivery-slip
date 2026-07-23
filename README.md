# Valued Delivery Slip for Odoo 19 (Bon de Livraison Valorisé) 📦

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple.svg)
![License](https://img.shields.io/badge/License-LGPL_v3-blue.svg)

A clean, light, and robust Odoo 19 module that adds pricing, discount, and tax details to the standard **Delivery Slip (Bon de Livraison)** report.

By default, Odoo's Delivery Slip only displays product quantities (ordered and delivered). This module inherits the standard report to display complete financial information when the delivery is linked to a **Sales Order (Bon de commande)**.

---

## ✨ Features

- **Pricing Columns Added**:
  - **Prix unitaire** (Unit Price)
  - **Rem. %** (Discount percentage with `%` suffix)
  - **Taxes** (Applicable taxes)
  - **Montant** (Subtotal amount per line)
- **Totals Summary**: Displays the financial totals at the bottom (aligned below the table and above the signature):
  - **Montant hors taxes** (Untaxed Amount)
  - **Taxes Breakdown** (e.g. TVA 19%, 10%)
  - **Total** (Total amount including taxes)
- **Conditional Visibility**: Financial columns and totals are only visible if the delivery is linked to a Sales Order. For internal transfers or inventory receipts, it automatically falls back to showing standard non-valued quantities.
- **Aggregated & Lot Compatibility**: Supports both aggregated product lines and individual serial/lot tracked line templates without breaking layout alignment.
- **Pure QWeb Module**: Zero custom Python tables, model overrides, or database changes, making it lightweight and highly compatible with other modules.

---

## 🛠️ Technical Details

- **Backend**: XML (QWeb Inheritance)
- **Report Template Inherited**: `stock.report_delivery_document`
- **Dependencies**: 
  - `stock` (Inventory transfers)
  - `sale_stock` (Connects pickings to Sales Orders and enables sales prices)
- **Compatibility**: Odoo 19.x

---

## 🚀 Installation & Setup

1. Copy or clone the `tahri_template_BL` folder into your custom Odoo addons directory.
2. Restart your Odoo server.
3. Log in to your Odoo instance as an **Administrator**.
4. Enable **Developer Mode**.
5. Navigate to **Apps** > Click **Update Apps List**.
6. Search for `Tahri Template BL` and click **Activate**.

---

## 💻 Usage

1. Create a **Sales Order** with product prices, discounts, and taxes.
2. Confirm the order to generate the **Delivery Order**.
3. Navigate to the Delivery Order (`stock.picking`) in the Inventory app.
4. Click **Print** > **Delivery Slip** (Bon de livraison).
5. The generated PDF will automatically display the pricing and tax details.

---

## 📄 License

This project is licensed under the LGPL-3 License.
