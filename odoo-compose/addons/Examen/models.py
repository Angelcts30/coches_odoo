# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class vehiculos(models.Model):
    _name = 'examen.vehiculos'
    _description = 'vehiculos'

    name = fields.Char(string="Matricula", required=True)
    color = fields.Char(string="Color", required=True)
    cantidad_asientos = fields.Integer(string="Cantidad de asientos", required=True)
    n_viajes = fields.Integer(string="Numero de viajes", required=True)
    seguro = fields.Boolean(string="Seguro", required=True)
    