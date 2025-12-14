# -*- coding: utf-8 -*-
from odoo import models, api, fields

class ProcurementGroup(models.Model):
    """Normalize custom move_type when procurement groups are created.

    If an external caller sets `move_type='pack_direct_ship_one'` (a
    module-only semantic value), convert it to the core-supported value
    `'direct'` before creating the record so downstream pickings don't
    receive an invalid value.
    """
    _inherit = 'procurement.group'

    move_type = fields.Selection(
        selection_add=[(
            'pack_direct_ship_one',
            'Pack products as soon as available, ship all products at once'
        )],
        ondelete={'pack_direct_ship_one': 'set default'},
        default='direct'
    )

    @api.model
    def create(self, vals):
        # Convert the module-specific label to a core move_type to avoid
        # writing an unknown value into persisted records (which raises).
        if vals.get('move_type') == 'pack_direct_ship_one':
            vals['move_type'] = 'direct'
        return super(ProcurementGroup, self).create(vals)