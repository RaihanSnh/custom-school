from odoo import fields, models

class Course(models.Model):
    _name = 'custom.school.course'
    _description = 'Data Course'

    name = fields.Char(
        string='Course Name',
        required=True,
        help="Fill course name here"
    )

    description = fields.Text(
        string='Description',
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    category_id = fields.Many2one(
        comodel_name='custom.school.category',
        string='Category', 
        #required=True 
    )
    