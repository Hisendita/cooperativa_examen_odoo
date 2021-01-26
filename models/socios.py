# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class socios(models.Model):
    _name = 'cooperativa_examen.socios'
    _description = 'Socios'
    _sql_constraints = [
        ("socios_id_socios_uniq","UNIQUE(id_socios)","No puede haber dos id_socios iguales."),
        ("socios_dni_uniq","UNIQUE(dni)","No puede haber dos DNI iguales."),
    ]


    id_socios = fields.Integer(string="ID", required=True)
    foto = fields.Binary()
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True, size=9)
    fecha_alta = fields.Datetime(string="Fecha", required=True, default=datetime.now())
    telf = fields.Integer(string="Telefono", required=True, size=9)
    email = fields.Char(string="Email")
    saldo = fields.Integer(string="Saldo", compute="calc_saldo", store=True)
    reg_pendientes = fields.One2many("cooperativa_examen.campanya", "campanya", string="Registros pendientes")

    @api.constrains("dni")
    def check_dni(self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = self.dni[-1]
        num = int(self.dni[:-1])
        if letras[num%23] != letra:
            raise ValidationError("Error. DNI invalido.")
    
    @api.constrains("email")
    def check_email(self):
        if "@" not in self.email and len(self.email) < 5:
            raise ValidationError("Error. Formato de e-mail invalido.")

    