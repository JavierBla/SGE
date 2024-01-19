# -*- coding: utf-8 -*-

from odoo import models, fields, api


class escuelasdevela_escuela(models.Model):
    _name = 'escuelasdevela.escuela'
    _description = 'Escuela'

    name = fields.Char(string="Denominación",required=True)
    logotipo = fields.Binary(string="Logotipo")
    email = fields.Char(string="Correo Electrónico", required=True)
    telefono = fields.Char(string="Teléfono de contacto", required=True)
    monitor = fields.Many2many("escuelasdevela.monitor",string="Monitor")
    alumno = fields.One2many("escuelasdevela.alumno","escuela",string="Alumno")
    curso = fields.One2many("escuelasdevela.curso","escuela",string="Curso")

class escuelasdevela_curso(models.Model):
    _name = 'escuelasdevela.curso'
    _description = 'Curso'

    name = fields.Char(string="Título",required=True)
    duracionDias = fields.Integer(string="Duración en días",required=True)
    duracionHoras = fields.Integer(string="Duración en horas",required=True)
    precio = fields.Float(string="Precio",required=True)
    escuela = fields.Many2one("escuelasdevela.escuela",string="Escuela")

class escuelasdevela_monitor(models.Model):
    _name = 'escuelasdevela.monitor'
    _description = 'Monitor'

    id = fields.Integer(string="ID",required=True,unique=True)
    name = fields.Char(string="Nombre",required=True)
    email = fields.Char(string="Correo Electrónico", required=True)
    telefono = fields.Char(string="Teléfono de contacto", required=True)
    escuela = fields.Many2many("escuelasdevela.escuela",string="Escuela")

class escuelasdevela_alumno(models.Model):
    _name = 'escuelasdevela.alumno'
    _description = 'Alumno'

    name = fields.Char(string="Nombre",required=True)
    email = fields.Char(string="Correo Electrónico",required=True)
    telefono = fields.Char(string="Teléfono de contacto",required=True)
    numMatricula = fields.Char(string="Número de matrícula",required=True)
    escuela = fields.Many2one("escuelasdevela.escuela",string="Escuela",required=True)