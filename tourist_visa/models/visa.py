# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class touristVisa(models.Model):
    _inherit = 'res.partner'
    _description = 'visa partner'
    visa_code = fields.Char('Code')
    fname = fields.Char('First Name')
    lname = fields.Char('Last Name')
    mname = fields.Char('Middle Name')
    # restaurant_item = fields.Boolean('Restaurant Item')
    my_visa = fields.Boolean('visa filter')
    nationality_id = fields.Many2one('res.country', ondelete='cascade', string="Nationality", required=True)
    destenation = fields.Many2one('res.country', ondelete='cascade', string="Destenation", required=True)
    STATUS_SELECTION = [
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('expired', 'Expired'),
    ]

    status = fields.Selection(selection=STATUS_SELECTION, string='Status')
    passport_number = fields.Char(string='Passport Number')
    issue_date = fields.Date(string='Issue Date')
    expiry_date = fields.Date(string='Expiry Date')
    visa_type = fields.Selection([
        ('tourist', 'Tourist Visa'),
        ('business', 'Business Visa'),
        ('student', 'Student Visa'),
        ('work', 'Work Visa'),
        ('transit', 'Transit Visa')
    ], string='Visa Type')
    # applicant_id = fields.Many2one('res.partner', string='Applicant')
    visa_code = fields.Char(string='Visa Code', compute='_compute_visa_code', store=True)

    @api.depends('country_id','destenation')
    def _compute_visa_code(self):
        for visa in self:
            country_code = visa.country_id.code if visa.country_id else ''
            passport_suffix = visa.passport_number[-4:] if visa.passport_number else ''
            sequence = int(datetime.timestamp(datetime.now()))
            visa.visa_code = f"{country_code}-{passport_suffix}-{sequence}"



