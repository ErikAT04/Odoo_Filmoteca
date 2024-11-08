#-*- coding: utf-8 -*-

from odoo import models, fields, api

class tecnica(models.Model):
    _name = 'filmotecaerik.tecnica'
    _description = 'filmotecaerik.tecnica'

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    photo = fields.Image(string="Imagen")
    peliculas_ids = fields.Many2many("filmotecaerik.pelicula", string="Peliculas", relation = "tecnicas_peliculas", column1 = "peliculas_ids", column2 = "tecnicas_ids")
