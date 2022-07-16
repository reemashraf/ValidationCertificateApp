from odoo import models, fields, api ,_


class CertificateType(models.Model):

    _name = 'certificate.type'

    name= fields.Char('Name')
