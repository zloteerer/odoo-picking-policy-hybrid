# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    # Add a new picking_policy option used by other parts of the module.
    _inherit = "sale.order"

    picking_policy = fields.Selection(
        selection_add=[(
            'pack_direct_ship_one',
            'Pack products as soon as available, ship all products at once'
        )],
        ondelete={'pack_direct_ship_one': 'set default'},
    )

    def _action_confirm(self):
        # After confirming a sale, enforce move_type decision for existing pickings
        # when the custom picking policy is selected.
        super(SaleOrder, self)._action_confirm()

        if self.picking_policy == 'pack_direct_ship_one':
            self._set_move_type_based_on_destination()

    def _set_move_type_based_on_destination(self):
        # Set move_type for sale's pickings based on whether each picking
        # is the final delivery to the customer.
        for picking in self.picking_ids:
            is_final_delivery = self._is_final_customer_delivery(picking)

            if is_final_delivery:
                picking.write({'move_type': 'one'})
            else:
                picking.write({'move_type': 'direct'})

    def _is_final_customer_delivery(self, picking):
        # True if the picking delivers directly to the customer or has no next moves.
        if picking.location_dest_id.usage == 'customer':
            return True

        if picking.picking_type_code == 'outgoing':
            next_moves = picking.move_ids_without_package.mapped('move_dest_ids')
            if not next_moves:
                return True

        return False
