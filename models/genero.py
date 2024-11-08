#-*- coding: utf-8 -*-

from odoo import models, fields, api

class genero(models.Model):
    _name = 'filmotecaerik.genero'
    _description = 'filmotecaerik.genero'

    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Char(string="Descripción") #Añado el nombre "Descripción" al campo (Para que no ponga Description en las tablas)

    peliculas_id = fields.One2many(string="Peliculas", comodel_name="filmotecaerik.pelicula", inverse_name="genero_id")