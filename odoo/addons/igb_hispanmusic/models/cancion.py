from odoo import models, fields

class Cancion(models.Model):
    _name = 'igb_hispanmusic.cancion'
    _description = 'Canción Musical'

    nombre = fields.Char(string='Nombre', required=True)
    portada = fields.Image(string='Portada')
    spotify = fields.Char(string='Spotify')
    youtube = fields.Char(string='YouTube')
    applemusic = fields.Char(string='Apple Music')
