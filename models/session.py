from odoo import api, fields, models, exceptions

class Session(models.Model):
    _name = 'custom.school.session'
    _description = 'Data Course Session'

    name = fields.Char(string='Name')
    course_id = fields.Many2one(comodel_name='custom.school.course', string='Course')

    teacher_id = fields.Many2one(comodel_name='res.partner', string='Teacher', domain="[('is_teacher', '=', True)]",)

    session_date = fields.Datetime(string='Session Date', default=fields.Datetime.now())

    min_participant = fields.Integer(string='Minimum Participant')

    participant_ids = fields.One2many(comodel_name='custom.school.participant', inverse_name='session_id', string='Participant')

    taken_seats = fields.Float(compute='_compute_taken_seats', string='Taken Seats', store=True)

    
    status = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'), ('approve', 'Approve'), ('complete', 'Complete'), ('cancel', 'Cancel')],
        readonly=True,
        default='draft',
        required=True
    )

    def action_approve(self):
        self.write({'status':'approve'})

    def action_complete(self):
        self.write({'status':'complete'})

    def action_cancel(self):
        self.write({'status':'cancel'})

    def action_reset(self):
        self.write({'status':'draft'})
    
    
    @api.depends('min_participant', 'participant_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_participant:
               record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.participant_ids) / record.min_participant


    @api.onchange('min_participant', 'participant_ids')
    def _onchange_participant(self):
        if self.min_participant < 0:
            return {
                'warning': {
                    'title': "Wrong Data!",
                    'message': "Min Participant can't be lower than zero",
                },
            }
        if self.min_participant < len(self.participant_ids):
           return{
               'warning': {
                   'title': "Too many participants",
                   'message': "Increase min participants or remove excess participants"
               },
           } 
        
    _sql_constains = [
        ('name_unique',
         'UNIQUE(name)',
         "Session Name Should Be Unique")
    ]

    @api.constrains('teacher_id', 'participant_ids')
    def _check_teacher_not_in_participants(self):
        for record in self:
            students = [r.student_id.id for r in record.participant_ids]
            if record.teacher_id and record.teacher_id in students:
                raise exceptions.ValidationError("Teacher can't be an Participant")
            
    def report_session(self):
        print("odooooo")
        return self.env.ref("custom_school.action_report_custom_school").report_action(self)
    
    # deactivate multi delete function
    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise exceptions.UserError("You can only delete when the session status is still in draft!")
        return super(Session, self).unlink()


class Participant(models.Model):
    _name = 'custom.school.participant'
    _description = 'Participant of Course Session..'

    name = fields.Char(string='Registration Number')
    student_id = fields.Many2one(
        comodel_name='res.partner',
        domain="[('is_student', '=', True)]",
        string='Student'
    )

    reg_date = fields.Datetime(string='Reg Date', default=fields.Datetime.now())

    session_id = fields.Many2one(comodel_name='custom.school.session', string='Session')

    remark = fields.Char(string='Remarks')