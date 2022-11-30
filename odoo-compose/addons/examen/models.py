# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class Vehiculos(models.Model):
    _name = 'examen.vehiculos'
    _description = 'Vehiculos'

    name = fields.Char(string="Nombre", required=True)
    color = fields.Char(string="Color", required=True)
    cantidad_asientos = fields.Integer(string="Cantidad de asientos", required=True)
    n_viajes = fields.Integer(string="Numero de viajes", required=True)
    seguro = fields.Boolean(string="Seguro", required=True)
    
class conductor(models.Model):
    _name = 'examen.conductor'
    _description = 'Conductor'
    

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    n_vehiculos = fields.Integer(string="Numero de vehiculos", required=True)


class seguro(models.Model):
    _name = 'examen.seguro'
    _description = 'Seguro'
    

    nombre_compania = fields.Char(string="Nombre de la compañia", required=True)
    fecha_vencimiento = fields.Date(string="Fecha de vencimiento", required=True)
    vehiculo = fields.Many2one('examen.vehiculos', string="Vehiculo")

class viaje(models.Model):
    _name = 'examen.viaje'
    _description = 'Viaje'
    

    nombre = fields.Char(string="Nombre", required=True)
    vehiculo = fields.Many2one('examen.vehiculos', string="Vehiculo")
    provincia_origen = fields.Char(string="Provincia_de_origen", required=True)
    provincia_destino = fields.Char(string="Provincia_de_destino", required=True)
    fecha = fields.Date(string="Fecha", required=True)
    duracion = fields.Integer(string="Duracion", required=True)
    duracion_mas_de_2_horas = fields.Boolean(string="Duracion_mas_de _2_horas", default=False)
    seguro_caducado = fields.Boolean(string="Seguro_caducado", default=False)

class provincia(models.Model):
    _name = 'examen.provincia'
    _description = 'Provincia'
    

    nombre = fields.Char(string="Nombre", required=True)
    
