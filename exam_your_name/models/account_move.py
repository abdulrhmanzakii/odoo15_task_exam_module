from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    product_id = fields.Many2one('product.template', string="Products")
