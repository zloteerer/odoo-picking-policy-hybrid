# -*- coding: utf-8 -*-
from odoo import models, api

class StockPicking(models.Model):
    # Apply custom picking policy rules on create and backorders.
    # This module sets `move_type` on pickings depending on sale.order policy.
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)

        # If the picking comes from a sale with our custom policy, decide move_type now.
        if picking.sale_id and picking.sale_id.picking_policy == 'pack_direct_ship_one':
            picking._set_move_type_based_on_destination()

        return picking

    def _set_move_type_based_on_destination(self):
        # For each picking, set move_type to 'one' when it is the final
        # customer delivery, otherwise use 'direct'.
        for picking in self:
            is_final_delivery = self._is_final_customer_delivery(picking)

            if is_final_delivery:
                picking.write({'move_type': 'one'})
            else:
                picking.write({'move_type': 'direct'})

    def _is_final_customer_delivery(self, picking):
        # Return True if this picking is the final delivery to the customer.
        if picking.location_dest_id.usage == 'customer':
            return True

        # If outgoing and there are no destination moves, it's final.
        if picking.picking_type_code == 'outgoing':
            next_moves = picking.move_ids_without_package.mapped('move_dest_ids')
            if not next_moves:
                return True

        return False

    def _create_backorder(self):
        backorders = super(StockPicking, self)._create_backorder()

        # Apply policy to created backorders when appropriate.
        for backorder in backorders:
            if backorder.sale_id and backorder.sale_id.picking_policy == 'pack_direct_ship_one':
                backorder._set_move_type_based_on_destination()

        return backorders