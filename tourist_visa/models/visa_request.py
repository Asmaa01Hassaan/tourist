from odoo import models, fields, api
from datetime import datetime

class visaRequest(models.Model):
    _name='visa.request'
    _description='STS visa request information'
    partner_id = fields.Many2one('res.partner', string='Partner')


    visa_code = fields.Char(string='Visa Code', compute='_compute_visa_code', store=True)
    ir_attachment_id = fields.Many2many('ir.attachment', string='Related attachment', required=True, ondelete='cascade')
    name = fields.Char(related='partner_id.name')
    destenation = fields.Many2one('visa.destination', ondelete='cascade', string="Destination", required=True)
    issue_date = fields.Date(string='Issue Date')
    expiry_date = fields.Date(string='Expiry Date')
    STATUS_SELECTION = [
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]
    status = fields.Selection(selection=STATUS_SELECTION, string='Status')
    visa_type = fields.Selection([
        ('tourist', 'Tourist Visa'),
        ('business', 'Business Visa'),
        ('student', 'Student Visa'),
        ('work', 'Work Visa'),
        ('transit', 'Transit Visa')
    ], string='Visa Type')
    @api.depends('destenation')
    def _compute_visa_code(self):
        for visa in self:
            country_code = visa.destenation.code if visa.destenation else ''
            passport_suffix = visa.partner_id.passport_number[-4:] if visa.partner_id.passport_number else ''
            sequence = int(datetime.timestamp(datetime.now()))
            visa.visa_code = f"{country_code}-{passport_suffix}-{sequence}"
