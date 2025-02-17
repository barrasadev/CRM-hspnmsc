# Author: Ivan Gonzalez Barrasa (barrasa.dev)
# File: cancion.py
# Path: ~/Proyectos/HispanMusic/CRM-hspnmsc/odoo/addons/igb_hispanmusic/models
# Created: 2025-02-14 15:51
# Last Updated: 2025-02-14 15:51

from odoo import models, fields

class Cancion(models.Model):
    _name = 'igb_hispanmusic.cancion'
    _description = 'Canción Musical'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    portada = fields.Image(string='Portada')
    spotify = fields.Char(string='Spotify')
    youtube = fields.Char(string='YouTube')
    applemusic = fields.Char(string='Apple Music')
