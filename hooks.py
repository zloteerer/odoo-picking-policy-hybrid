# -*- coding: utf-8 -*-
import logging

_logger = logging.getLogger(__name__)


def uninstall_hook(cr, registry):
    """Cleanup picking_policy values set to 'pack_direct_ship_one' during module uninstall."""
    _logger.info("Running uninstall_hook for picking_policy_hybrid module")
    cr.execute("""
        UPDATE ir_default
        SET json_value = '"one"'
        WHERE field_id IN (
            SELECT id FROM ir_model_fields
            WHERE name = 'picking_policy'
            AND model = 'sale.order'
        )
    """)
    _logger.info("uninstall_hook: Cleaned up 'pack_direct_ship_one' picking_policy values.")
