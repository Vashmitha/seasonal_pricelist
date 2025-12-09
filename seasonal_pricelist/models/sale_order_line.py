from odoo import models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _get_order_date(self):
        self.ensure_one()
        if self.order_id.is_delivery_date_based_price and self.order_id.commitment_date:
            return self.order_id.commitment_date
        return self.order_id.date_order