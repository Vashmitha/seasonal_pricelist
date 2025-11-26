from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_delivery_date_based_price = fields.Boolean(
        string='Is price based on Delivery date',
        tracking=True,
    )

    @api.constrains('is_delivery_date_based_price', 'commitment_date')
    def _check_commitment_date_required(self):
        for order in self:
            if order.is_delivery_date_based_price and not order.commitment_date:
                raise ValidationError(
                    _("Commitment Date is required when 'Price based on Delivery date' is enabled.\n"
                      "Add the delivery date in the Other Info tab under the Delivery section.")
                )