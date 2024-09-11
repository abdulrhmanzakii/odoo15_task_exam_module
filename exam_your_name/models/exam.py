from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date





class YourExam(models.Model):
    _name = "your.exam"
    _description = "Your exam"
    _rec_name = "name"

    name = fields.Many2one('hr.employee',string="Name",required=True)
    start_date = fields.Date(string="Start Date",default=fields.Datetime.today)
    end_date = fields.Date(string="end Date",required=True)
    mark = fields.Float(string="Mark")
    state = fields.Selection([
        ('created', 'Created'),
        ('solved', 'Solved'),
        ('finished', 'Finished'),
        ('canceled', 'Canceled')], string="Statues", required=True, default='created', tracking=True)
    active = fields.Boolean(string="Active", default=True)
    exam_type_id = fields.Many2one('exam.type',string="Exam Type")
    serial_num = fields.Integer(related="exam_type_id.serial")


    @api.constrains('start_date','end_date')
    def check_end_date(self):
        for rec in self:
            if rec.start_date and rec.start_date > rec.end_date:
                raise ValidationError(_("THE DATE YOU HAD ENTERED IS NOT ACCEPTABLE!"))

    def action_solve(self):
        for rec in self:
            rec.state = 'solved'

    def action_back_to_created(self):
        for rec in self:
            rec.state = 'created'

    def action_finished(self):
        for rec in self:
            rec.state = 'finished'
    def action_back_to_solved(self):
        for rec in self:
            rec.state = 'solved'

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'

    def action_reset_to_created(self):
        for rec in  self:
            rec.state = 'created'