from odoo import models, fields, api ,_


class TrafficDepartment(models.Model):

    _name = 'traffic.department'

    name= fields.Char('Name')
