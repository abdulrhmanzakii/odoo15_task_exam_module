from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date



class ExamType(models.Model):
    _name = "exam.type"
    _description = "Exam Type"
    _rec_name = "name"

    name = fields.Char(string="Name",required=True)
    serial = fields.Integer("Serial Number")
    state = fields.Selection([
        ('draft','Draft'),
        ('finished','Finished')],default='draft')

