#-*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api

class pelicula(models.Model):
    _name = 'filmotecaerik.pelicula'
    _description = 'filmotecaerik.pelicula'

    codigo_peli = fields.Char(string="Código", compute = "_get_code")
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    film_date = fields.Date(string="Fecha de grabación")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")
    language = fields.Selection(selection=[('español', 'Español'), ('ingles', 'Inglés'), ('aleman', 'Alemán'), ('frances', 'Francés')], default='español', required = True, string="Idioma")
    opinion = fields.Selection(selection=[('0', 'mala'), ('1', 'regular'), ('2', 'buena')], default='2', required = True, string="Opinión")
    color = fields.Selection(selection=[('0', 'Blanco y negro'), ('1', 'Color')], default = '0', required = True, string="Tipo de color")
    image = fields.Image(string="Imagen")
    genero_id = fields.Many2one("filmotecaerik.genero", string="Género", required = True, ondelete = "cascade")
    tecnicas_ids = fields.Many2many("filmotecaerik.tecnica", string="Técnicas", relation = "tecnicas_peliculas", column1 = "tecnicas_ids", column2 = "peliculas_ids")
    colorbool = fields.Boolean(string="Color Booleano")
    is_spanish = fields.Boolean(string = "En español")


    def _get_code(self):
        for pelicula in self:
            if len(pelicula.genero_id) == 0:
                pelicula.codigo_peli = f"FILM_{str(pelicula.id)}"
            else:
                pelicula.codigo_peli = str(pelicula.genero_id.name) + "_" + str(pelicula.id)
    
    def toggle_color(self):
        self.colorbool = not self.colorbool

    def f_create(self):
        pelicula = {
            "name" : "Prueba ORM",
            "colorbool" : True,
            "genero_id":1,
            "start_date": str(datetime.date(2022,8,8))
        }
        print(pelicula)
        self.env['filmotecaerik.pelicula'].create(pelicula)
    
    def f_modify(self):
        pelicula = {
            "name" : f"{self.name}_mod",
            "description" :f"{self.description}_modificado",
        }
        self.write(pelicula)
    
    def f_delete(self):
        self.unlink()