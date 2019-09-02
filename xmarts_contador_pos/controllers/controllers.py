# -*- coding: utf-8 -*-
from odoo import http

# class XmartsContadorPos(http.Controller):
#     @http.route('/xmarts_contador_pos/xmarts_contador_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xmarts_contador_pos/xmarts_contador_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xmarts_contador_pos.listing', {
#             'root': '/xmarts_contador_pos/xmarts_contador_pos',
#             'objects': http.request.env['xmarts_contador_pos.xmarts_contador_pos'].search([]),
#         })

#     @http.route('/xmarts_contador_pos/xmarts_contador_pos/objects/<model("xmarts_contador_pos.xmarts_contador_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xmarts_contador_pos.object', {
#             'object': obj
#         })