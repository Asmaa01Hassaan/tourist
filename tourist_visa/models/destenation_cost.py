# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class costDestination(models.Model):
    _name='cost.destination'
    _description='STS cost destination Mangement'

    name=fields.Char(string='Period')
    cost=fields.Monetary(string='cost', default=0.0 , currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default =lambda self:self.env.company.currency_id.id)

