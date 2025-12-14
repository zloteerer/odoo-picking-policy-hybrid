# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettingsExtension(models.TransientModel):
    """Expose sale.order and add a label to default `picking_policy` in Settings UI."""
    _inherit = 'res.config.settings'

    default_picking_policy = fields.Selection(
        selection_add=[(
            'pack_direct_ship_one',
            'Pack products as soon as available, ship all products at once'
        )],
        ondelete={'pack_direct_ship_one': 'set default'},
        default="direct"
    )