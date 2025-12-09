from odoo import models, fields, api, _
from odoo.exceptions import UserError

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
                raise UserError(_("Delivery Date is required when price based on Delivery date is enabled."))

    @api.onchange('commitment_date', 'is_delivery_date_based_price')
    def _onchange_update_pricelist(self):
        for order in self:
            if order.is_delivery_date_based_price and order.commitment_date:
                seasonal_pricelist = self.env['product.pricelist'].search([('name', 'ilike', 'Seasonal Pricelist')], limit=1)
                if not seasonal_pricelist:
                    return {
                        'warning': {
                            'title': _("Missing Pricelist"),
                            'message': _("Create a pricelist named Seasonal Pricelist.")
                        }
                    }
                order.pricelist_id = seasonal_pricelist
                order.show_update_pricelist = True