# -*- coding: utf-8 -*-
# from odoo import http


# class CooperativaExamen(http.Controller):
#     @http.route('/cooperativa_examen/cooperativa_examen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cooperativa_examen/cooperativa_examen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cooperativa_examen.listing', {
#             'root': '/cooperativa_examen/cooperativa_examen',
#             'objects': http.request.env['cooperativa_examen.cooperativa_examen'].search([]),
#         })

#     @http.route('/cooperativa_examen/cooperativa_examen/objects/<model("cooperativa_examen.cooperativa_examen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cooperativa_examen.object', {
#             'object': obj
#         })
