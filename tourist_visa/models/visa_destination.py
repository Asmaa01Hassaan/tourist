# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class visaDestination(models.Model):
    _name='visa.destination'
    _description='STS visa destination Mangement'
    _rec_name='country_id'

    country_id = fields.Many2one('res.country', ondelete='cascade', string="Name", required=True)

    # code = country_id.id.code
    code = fields.Char(compute='_get_country_code', store=True)
    @api.depends('country_id')
    def _get_country_code(self):
        self.code = self.country_id.code if self.country_id else ''
