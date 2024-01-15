from odoo import api, fields, models

class Session(models.Model):
    _name = 'custom.school.session'
    _description = 'Data Course Session'

    name = fields.char(string='Name')
    course_id = fields.Many2one(comodel_name='custom.school.course', string='Course')

    teacher_id = fields.Many2one(comodel_name='res.partner', string='Teacher', domain="[('is_teacher', '=', True)]",)

    session_date = fields.Datetime(string='Session Date', default=fields.Datetime.now())

    min_participant = fields.Integer(string='Minimum Participant')

    participant_ids = fields.One2many(comodel_name='custom.school.participant', inverse_name='session_id', string='Participant')

class Participant(models.Model):
    _name = 'custom.school.articipant'
    _description = 'Participant of Course Session..'

    name = fields.Char(string='Registration Number')
    student_id = fields.Many2one(
        comodel_name='model.name',
        domain="[('is_student' '=', True)]"
        string='Student',
    )

    reg_date = fields.Datetime(string='Reg Date', default=fields.Datetime.now())

    session_id = fields.Many2one(comodel_name='custom.school.session', string='Session')

    remark = fields.Char(string='Remarks')
    

    
    