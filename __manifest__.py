# -*- coding: utf-8 -*-
{
    'name': "Picking Policy Hybrid - Pack Direct Ship One",
    'summary': 'Pack direct, ship complete picking policy',
    'description': """
Pack Direct Ship One Policy
===========================

Adds a new picking policy: 'pack_direct_ship_one'

- Pack operations: Direct mode
- Ship operations: One/Complete mode

Reduces partial customer deliveries while maintaining internal warehouse flexibility.
""",
    'author': "zloteerer",
    'website': "github.com/zloteerer",
    'category': 'Operations/Inventory',
    'version': '15.0.1.0.0',
    'depends': ['sale_stock', 'stock', 'base'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'uninstall_hook': 'uninstall_hook',
}