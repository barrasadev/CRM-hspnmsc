from odoo import models, fields

class Artista(models.Model):
    _name = 'igb_hispanmusic.artista'
    _description = 'Artista Musical'

    nombre_real = fields.Char(string='Nombre Real', required=True)
    nombre_artistico = fields.Char(string='Nombre Artístico', required=True)
    foto = fields.Image(string='Foto')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    canciones_ids = fields.Many2many('igb_hispanmusic.cancion', string='Canciones')
    spotify = fields.Char(string='Spotify')
    youtube = fields.Char(string='YouTube')
    instagram = fields.Char(string='Instagram')
    applemusic = fields.Char(string='Apple Music')
