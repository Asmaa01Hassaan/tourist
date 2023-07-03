# -*- coding: utf-8 -*-
# from odoo import http


# class TouristVisa(http.Controller):
#     @http.route('/tourist_visa/tourist_visa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tourist_visa/tourist_visa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tourist_visa.listing', {
#             'root': '/tourist_visa/tourist_visa',
#             'objects': http.request.env['tourist_visa.tourist_visa'].search([]),
#         })

#     @http.route('/tourist_visa/tourist_visa/objects/<model("tourist_visa.tourist_visa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tourist_visa.object', {
#             'object': obj
#         })
