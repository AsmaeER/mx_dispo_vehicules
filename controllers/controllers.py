# -*- coding: utf-8 -*-
from odoo import http

class MxWebsite(http.Controller):
    @http.route('/dispo_vehicules/dispo_vehicules/', auth='public', website=True)
    def index(self, **kw):
        vehicle = http.request.env['fleet.vehicle'].search('state_id', '=', "Disponible")
        return http.request.render('mx_website.index', {
            'Vehicles': vehicle.search([]),
        })

#     @http.route('/mx_dispo_vehicules/mx_dispo_vehicules/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mx_dispo_vehicules.listing', {
#             'root': '/mx_dispo_vehicules/mx_dispo_vehicules',
#             'objects': http.request.env['mx_dispo_vehicules.mx_dispo_vehicules'].search([]),
#         })

#     @http.route('/mx_dispo_vehicules/mx_dispo_vehicules/objects/<model("mx_dispo_vehicules.mx_dispo_vehicules"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mx_dispo_vehicules.object', {
#             'object': obj
#         })