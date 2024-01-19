# -*- coding: utf-8 -*-
# from odoo import http


# class Escuelasdevela(http.Controller):
#     @http.route('/escuelasdevela/escuelasdevela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuelasdevela/escuelasdevela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuelasdevela.listing', {
#             'root': '/escuelasdevela/escuelasdevela',
#             'objects': http.request.env['escuelasdevela.escuelasdevela'].search([]),
#         })

#     @http.route('/escuelasdevela/escuelasdevela/objects/<model("escuelasdevela.escuelasdevela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuelasdevela.object', {
#             'object': obj
#         })
