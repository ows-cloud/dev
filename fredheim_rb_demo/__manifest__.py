# Copyright 2023 Ows - Henrik Norlin
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Fredheim Resource Booking Demo",
    "summary": "",
    "author": "Ows, Odoo Community Association (OCA)",
    "category": "Uncategorized",
    "demo": [
        "demo/demo.xml",
        "views/resource_booking_views.xml",
    ],
    "depends": [
        "contacts",
        "sale_management",
        "website_sale_resource_booking",  # oca/calendar, oca/sale-workflow, oca/e-commerce
        "partner_product_price",  # oca/product-attribute
        "sale_resource_booking_product_variant",
        "sale_resource_booking_timeline",
    ],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "maintainers": ["ows-cloud"],
    "version": "16.0.1.0.0",
    "website": "https://github.com/OCA/",
}
