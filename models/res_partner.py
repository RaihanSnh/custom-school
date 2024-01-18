from odoo import api, fields, models

class  Partner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(
        string='Student',
        default=False
    )

    is_teacher = fields.Boolean(
        string='Teacher',
        default=False
    )