from odoo import models, fields

class Artista(models.Model):
    _name = 'igb_hispanmusic.artista'
    _description = 'Artista Musical'

    nombre_real = fields.Char(string='Nombre Real', required=True)
    nombre_artistico = fields.Char(string='Nombre Artístico', required=True)
    foto = fields.Image(string='Foto', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')

    canciones_ids = fields.Many2many('igb_hispanmusic.cancion', string='Canciones')
    spotify = fields.Char(string='Spotify')
    youtube = fields.Char(string='YouTube')
    instagram = fields.Char(string='Instagram')
    applemusic = fields.Char(string='Apple Music')

    referido_por_id = fields.Many2one('igb_hispanmusic.artista', string='Referido por', domain="[('id', '!=', id)]", ondelete='set null')
    saldo_afiliado = fields.Float(string='Saldo Afiliado', default=0.00, digits=(10,2), help="Saldo acumulado por el artista como afiliado", readonly=False)