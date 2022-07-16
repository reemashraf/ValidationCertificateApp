from odoo import models, fields, api ,_
from datetime import datetime

class Certificate(models.Model):

    _name = 'certificate'

    print_certificate = fields.Boolean("Print Certificate",default=True)
    price = fields.Integer('Price')
    motor_number = fields.Integer("Motor Number")
    chassis_number = fields.Char('Chassis Number')

    car_model = fields.Selection('_get_selection' ,'Car Model')
    serial_number = fields.Char('Serial Number',required=True ,copy=False,readonly=True,index=True,
                                default=lambda self:_('New'))
    vehicle_type = fields.Selection([('car','Car'),('bus','Bus'),('minibus','Minibus'),('microbus','Microbus')] , 'Vehicle Number')


    brand = fields.Many2one('vehicle.brand','Brand')
    certificate_type_id = fields.Many2one('certificate.type','Certificate Type')
    traffic_department_id = fields.Many2one('traffic.department','Traffic Department')
    customer_id = fields.Many2one('res.partner','Customer')


    @api.model
    def create(self, vals_list):
        if vals_list.get('serial_number',_('New')) == _('New'):
            vals_list['serial_number'] = self.env['ir.sequence'].next_by_code(
                'certificate') or _('New')
        return super(Certificate,self).create(vals_list)

    def _get_selection(self,context=None):
        current_year = datetime.today().year
        return [(str(current_year-ele) , str(current_year-ele)) for ele in range(20)]


    def action_print(self):
        self.ensure_one()
        self.print_certificate = False
        print(self.env.user)
        vals = {
            'certificate_id':self.id,
            'user_id':self.env.user.id,}
        log = self.env['print.certificate.log'].create(vals)
        return self.env.ref('CertificateApp.action_certificate_template').report_action(self)

    def action_allow_reprint(self):
        self.print_certificate = True