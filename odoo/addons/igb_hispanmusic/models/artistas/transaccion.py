# Author: Ivan Gonzalez Barrasa (barrasa.dev)
# File: transaccion.py
# Path: ~/Proyectos/HispanMusic/CRM-hspnmsc/odoo/addons/igb_hispanmusic/models/artistas
# Created: 2025-02-17 12:11
# Last Updated: 2025-02-17 12:11

from odoo import models, fields

class Transaccion(models.Model):
    _name = 'igb_hispanmusic.transaccion'
    _description = 'Registro de Transacciones'
    _order = 'fecha desc'
    _rec_name = 'mensaje'

    artista_id = fields.Many2one(
        'igb_hispanmusic.artista',
        string="Artista",
        required=True,
        ondelete='cascade'
    )
    tipo_transaccion = fields.Selection([
        ('ingreso', 'Ingreso'),
        ('retiro', 'Retiro'),
    ], string="Tipo de Transacción", required=True)

    importe = fields.Float(string="Importe", required=True)
    mensaje = fields.Char(string="Mensaje", required=True)
    fecha = fields.Datetime(string="Fecha", default=fields.Datetime.now, readonly=True)
