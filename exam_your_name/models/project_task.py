from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "project.task"

    exam = fields.Char(string="Exam")
    res_partner_id = fields.Many2one('res.partner',string="Partner")
    gender = fields.Selection([('male','Male'),
                               ('female','Female')],string="Gender")




