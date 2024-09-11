from odoo import api, fields, models


class Picking(models.Model):

    _inherit = "stock.picking"
