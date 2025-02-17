# Author: Ivan Gonzalez Barrasa (barrasa.dev)
# File: artista.py
# Path: ~/Proyectos/HispanMusic/CRM-hspnmsc/odoo/addons/igb_hispanmusic/models
# Created: 2025-02-14 15:51
# Last Updated: 2025-02-14 15:51

from odoo import models, fields

class Artista(models.Model):
    _name = 'igb_hispanmusic.artista'
    _description = 'Artista Musical'
    _rec_name = 'nombre_artistico'

    nombre_real = fields.Char(string='Nombre Real', required=True)
    nombre_artistico = fields.Char(string='Nombre Artístico', required=True)
    foto = fields.Image(string='Foto', required=True)
    telefono = fields.Char(string='Telefono')
    telegram = fields.Char(string='Telegram')
    instagram = fields.Char(string='Instagram')
    email = fields.Char(string='Email')

    canciones_ids = fields.Many2many('igb_hispanmusic.cancion', string='Canciones')
    spotify = fields.Char(string='Spotify')
    youtube = fields.Char(string='YouTube')
    applemusic = fields.Char(string='Apple Music')

    referido_por_id = fields.Many2one(
        'igb_hispanmusic.artista',
        string="Referido por",
        domain="[('id', '!=', id)]"
    )
    saldo = fields.Float(
        string="Saldo",
        default=0.0,
        digits=(10, 2)
    )

    transacciones_ids = fields.One2many(
        'igb_hispanmusic.transaccion',
        'artista_id',
        string="Transacciones"
    )