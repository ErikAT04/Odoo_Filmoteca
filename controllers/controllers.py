# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecaerik(http.Controller):
#     @http.route('/filmotecaerik/filmotecaerik', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecaerik/filmotecaerik/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecaerik.listing', {
#             'root': '/filmotecaerik/filmotecaerik',
#             'objects': http.request.env['filmotecaerik.filmotecaerik'].search([]),
#         })

#     @http.route('/filmotecaerik/filmotecaerik/objects/<model("filmotecaerik.filmotecaerik"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecaerik.object', {
#             'object': obj
#         })
