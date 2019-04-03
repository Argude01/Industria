# -*- coding: utf-8 -*-
from odoo import http

# class ProyectoIndustria(http.Controller):
#     @http.route('/proyecto_industria/proyecto_industria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_industria/proyecto_industria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_industria.listing', {
#             'root': '/proyecto_industria/proyecto_industria',
#             'objects': http.request.env['proyecto_industria.proyecto_industria'].search([]),
#         })

#     @http.route('/proyecto_industria/proyecto_industria/objects/<model("proyecto_industria.proyecto_industria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_industria.object', {
#             'object': obj
#         })