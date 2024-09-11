from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date



class StudentEvaluation(models.Model):
    _name = "student.evaluation"
    _description = "Student Evaluation"
    _rec_name = "name"

    name = fields.Many2one('hr.employee',string="Name",required=True)
    student_grade= fields.Integer(string="Student Grade")
    final_grade= fields.Integer(string="Final grade")
    student_percentage= fields.Integer(string="Student Percentage",readonly=True,
                                       compute="_compute_student_percentage")
    evaluation= fields.Selection([('excellent','Excellent'),
                                  ('vgood','Vgood'),
                                  ('good','Good'),
                                  ('fair','Fair'),
                                  ('poor','Poor'),('nottested','not tested'),], string="Evaluation",readonly=True,
                                 compute="_compute_evaluation")

    @api.depends('student_grade')
    def _compute_student_percentage(self):
        for rec in self:
           rec.student_percentage = rec.student_grade
        return

    @api.depends('student_percentage','student_grade')
    def _compute_evaluation(self):
        for rec in self:
            if rec.student_grade < 50:
               evaluation= 'poor'
            elif rec.student_grade == 50 or rec.student_grade <= 65:
                evaluation= 'fair'
            elif rec.student_grade == 66 or rec.student_grade <= 75:
                evaluation = 'good'
            elif rec.student_grade == 76 or rec.student_grade <= 85:
                evaluation = 'vgood'
            elif rec.student_grade == 100 or rec.student_grade <= 99:
                evaluation = 'excellent'
            else:
                raise ValidationError(_("The Number Can't Be Bigger Than 100"))

            rec.evaluation = evaluation

    @api.constrains('final_grade')
    def limit_grade(self):
        for rec in self:
           if rec.final_grade > 100:
                raise ValidationError(_("The Number Can't Be Bigger Than 100"))


