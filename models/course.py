from odoo import fields, models

class Course(models.Model):
    _name = 'custom_school'
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