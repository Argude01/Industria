# -*- coding: utf-8 -*-
from odoo import http

# class Usuario2(http.Controller):
#     @http.route('/usuario2/usuario2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/usuario2/usuario2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('usuario2.listing', {
#             'root': '/usuario2/usuario2',
#             'objects': http.request.env['usuario2.usuario2'].search([]),
#         })

#     @http.route('/usuario2/usuario2/objects/<model("usuario2.usuario2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('usuario2.object', {
#             'object': obj
#         })