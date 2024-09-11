from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = "sale.order"
    qunet=fields.Integer(string="Qunet")
    deg=fields.Integer(string="Degree")


