# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class fcties(models.Model):
#     _name = 'fcties.fcties'
#     _description = 'fcties.fcties'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class fcties_alumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Alumno'

    name = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    fechaNacimiento = fields.Date(string="Fecha de nacimiento",required=True)
    cursoAcademico = fields.Date(string="Curso Academico")
    email = fields.Char(string="Correo electrónico")
    telefono = fields.Char(string="Teléfono")
    ciclo = fields.Selection([("0","DAM"),("1","DAW"),("2","ASIX")],default="0",string="Ciclo formativo",required=True)
    periodo = fields.Selection([("0","Abril"),("1","Septiembre")],default="0",string="Periodo de práctica",required=True)
    notaMedia = fields.Float(string="Nota media",required=True)
    notaTexto = fields.Char(compute="nota_media_texto",string="Nota media en formato texto",store=True)
    empresa = fields.Many2one("fcties.empresa",string="Empresa")

    @api.depends('notaMedia')
    def nota_media_texto(self):
        for fcties_alumno in self:
            if fcties_alumno.notaMedia > 10:
                fcties_alumno.notaMedia = 10 
                
            if 5 <= fcties_alumno.notaMedia < 7:
                fcties_alumno.notaTexto = 'Aprobado'
            elif 7 <= fcties_alumno.notaMedia < 9:
                fcties_alumno.notaTexto = 'Notable'
            elif 9 <= fcties_alumno.notaMedia <= 10:
                fcties_alumno.notaTexto = 'Sobresaliente'
            else:
                fcties_alumno.notaTexto = 'Suspendido'

class fcties_empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'
    
    name = fields.Char(string="Nombre",required=True)
    pContacto = fields.Char(string="Persona de contacto",required=True)
    tContacto = fields.Char(string="Teléfono de contacto",required=True)
    email = fields.Char(string="Correo electrónico",required=True)
    direccion = fields.Char(string="Dirección",required=True)
    alumnos = fields.One2many("fcties.alumno","empresa",string="Alumnos")