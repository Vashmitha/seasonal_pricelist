from odoo import models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _get_order_date(self):
        self.ensure_one()
        price_date = (
            self.order_id.commitment_date
            if self.order_id.is_delivery_date_based_price and self.order_id.commitment_date
            else self.order_id.date_order
        )

        return price_date