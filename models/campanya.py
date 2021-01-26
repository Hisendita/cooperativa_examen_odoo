# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class companya(models.Model):
    _name = 'cooperativa_examen.campanya'
    _description = 'Campanya'

    fecha = fields.Datetime(string="Fecha", required=True, default=datetime.now())
    campanya = fields.Datetime(string="Campaña")
    cantidad = fields.Integer(string="Cantidad")
    producto = fields.Many2one("cooperativa_examen.productos","Producto")
    socio = fields.Many2one("cooperativa_examen.socios", "Socio")

    @api.constrains("cantidad")
    def check_cantidad(self):
        if self.cantidad < 0:
            raise ValidationError("Error. La cantidad debe ser mayor que 0.")

    def update_saldo(self):
        return True
    def update_kilos(self):
        return True
    def del_historial(self):
        return True