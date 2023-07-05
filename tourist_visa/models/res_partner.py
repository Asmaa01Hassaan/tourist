# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class touristVisa(models.Model):
    _inherit = 'res.partner'
    _description = 'visa partner'


    fname = fields.Char('First Name')
    lname = fields.Char('Last Name')
    mname = fields.Char('Middle Name')
    name = fields.Char(compute='_compute_full_name', store=True)
    # restaurant_item = fields.Boolean('Restaurant Item')
    my_visa = fields.Boolean('visa filter')
    nationality_id = fields.Many2one('res.country', ondelete='cascade', string="Nationality", required=True)

    passport_number = fields.Char(string='Passport Number')

    birth_date = fields.Date(string='Birth Date')

    gender_type = fields.Selection([
        ('null', ' '),
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    # applicant_id = fields.Many2one('res.partner', string='Applicant')

    ir_attachment_id = fields.Many2many('ir.attachment', string='Related attachment', required=True, ondelete='cascade')

    @api.depends('fname', 'lname')
    def _compute_full_name(self):
        self.name =f"{self.fname} {self.lname}"
