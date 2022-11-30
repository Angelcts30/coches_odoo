# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'coches_Examen.vehiculo'
    
    name = fields.Char(string="Matricula", required=True)
    marca = fields.Char(string="Marca", required=True)
    color = fields.Char(string="Color", required=True)
    cantidad_asientos = fields.Integer(string="Cantidad de asientos", required=True)
    viajes = fields.One2many('coches_Examen.viaje', 'vehiculo', string="Viajes")
    seguro = fields.Boolean(string="Seguro", required=True)
    
class conductor(models.Model):
    _name = 'coches_Examen.conductor'
    
    name = fields.Char(string="Nombre", required=True)
    dni = fields.Char(string="DNI", required=True)
    n_viajes = fields.Integer(string="Numero de viajes", required=True) 

class seguro(models.Model):
    _name = 'coches_Examen.seguro'
    
    name = fields.Char(string="Nombre", required=True)
    fecha_vencimiento_seguro = fields.Date(string="Fecha de vencimiento del seguro", required=True)
    vehiculo = fields.Many2one('coches_Examen.vehiculo', string="Vehiculo")

    

   
