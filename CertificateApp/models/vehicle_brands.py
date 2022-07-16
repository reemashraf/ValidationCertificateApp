from odoo import models, fields, api ,_


class VehicleBrands(models.Model):

    _name = 'vehicle.brand'

    name= fields.Char('Name')
