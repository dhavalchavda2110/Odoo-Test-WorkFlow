from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _create_orders_by_category(self, products):
        category_map = {}
        for product in products:
            cat = product.categ_id
            category_map.setdefault(cat, []).append(product)

        orders = []
        for cat, products in category_map.items():
            po = self.create({
                'partner_id': self.partner_id.id,
                'order_line': [(0, 0, {
                    'product_id': p.id,
                    'name': p.name,
                    'product_qty': 1,
                    'price_unit': p.list_price,
                    'product_uom': p.uom_id.id,
                    'date_planned': fields.Datetime.now(),
                }) for p in products]
            })
            orders.append(po)
        return orders
