from odoo import models, fields, api ,_
from datetime import datetime

class PrintCertificateLog(models.Model):

    _name = 'print.certificate.log'


    certificate_id = fields.Many2one('certificate')
    user_id = fields.Many2one('res.users')
    date = fields.Date(default=datetime.today())