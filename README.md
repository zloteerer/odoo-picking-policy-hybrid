
# Odoo Module - Picking Policy Hybrid

This Odoo module adds a small, focused picking-policy feature that lets
you pack products as soon as they are available while shipping all
products in a single delivery.

---

## Key features
- Adds a new `picking_policy` option on `sale.order`: `pack_direct_ship_one`.
- Exposes a `default_picking_policy` option in Settings so you can set the
	default behaviour for new sales.
- Normalises the module-specific label to core-supported values before
	creating persistent records, avoiding invalid selection errors.
- Applies `move_type` to pickings during creation and when creating backorders
	so the warehouse follows the chosen policy.

## Compatibility
- Only tested with Odoo 15 (should work on derivatives with the same models).
- Depends on: `sale_stock` (and the core `stock`/`sale` addons).

## Installation
1. Put the module folder into your Odoo `addons` path.
2. Restart Odoo and update the apps list.
3. Install `Picking Policy Hybrid` from Apps (or upgrade if already installed).

## Configuration
- Go to Settings → Inventory (Stock) and choose the preferred
	`Default Picking Policy` if you want to change the default for new orders.

## License
See project policy.

