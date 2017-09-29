# -*- coding: utf-8 -*-
from odoo import http

# class TickeleTest(http.Controller):
#     @http.route('/tickele_test/tickele_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tickele_test/tickele_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tickele_test.listing', {
#             'root': '/tickele_test/tickele_test',
#             'objects': http.request.env['tickele_test.tickele_test'].search([]),
#         })

#     @http.route('/tickele_test/tickele_test/objects/<model("tickele_test.tickele_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tickele_test.object', {
#             'object': obj
#         })