from odoo import fields, models

class Course(models.Model):
    _name = 'custom.school.course.category'
    _description = 'Data Course Category'

    name = fields.Char(
        string='Course Category Name',
        required=True,
        help="Fill course category name here"
    )

    description = fields.Text(
        string='Description',
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    course_ids = fields.One2many(
        string='Course',
        comodel_name='custom.school.course',
        inverse_name='category_id'
    )
    