# -*- coding: utf-8 -*-

from odoo import models, fields, api


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




