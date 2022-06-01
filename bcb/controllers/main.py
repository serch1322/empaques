# -*- coding: utf-8 -*-

from odoo import http
from odoo.addons.http_routing.models.ir_http import slug

class BCBWeb(http.Controller):

    @http.route(['/bcb/abc',], auth="public", website=True)
    def bcb(self, **kw):
        dias = ['lunes', 'martes', 'miercoles']
        return http.request.render('bcb.bcb_abc', {'dias_semana': dias})