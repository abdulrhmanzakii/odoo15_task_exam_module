from odoo import api, fields, models


class StockMove(models.Model):

    _inherit = "stock.move"

    barcode = fields.Char(related="product_id.barcode")
