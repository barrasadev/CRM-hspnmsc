from odoo import models, fields

class Transaccion(models.Model):
    _name = 'igb_hispanmusic.transaccion'
    _description = 'Registro de Transacciones'
    _order = 'fecha desc'

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
