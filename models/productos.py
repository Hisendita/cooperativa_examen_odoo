# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class productos(models.Model):
    _name = 'cooperativa_examen.productos'
    _description = 'Productos'
    _sql_constraints = [
        ("productos_nombre_uniq","UNIQUE(nombre)","No puede haber dos productos iguales."),
    ]

    nombre = fields.Char(string="Nombre", required=True)
    desc = fields.Char(string="Descripcion", required=True)
    precio = fields.Float(string="Precio", required=True)
    kilos_totales = fields.Float(string="Kilos Totales", default=0)

    @api.constrains("precio")
    def check_precio(self):
        if self.precio < 0:
            raise ValidationError("Error. El precio no puede ser negativo.")
    def del_kilos(self):
        return True