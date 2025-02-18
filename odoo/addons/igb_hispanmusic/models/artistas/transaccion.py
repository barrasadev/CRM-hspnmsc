from odoo import models, fields, api

class Transaccion(models.Model):
    _name = 'igb_hispanmusic.transaccion'
    _description = 'Registro de Transacciones'
    _rec_name = 'mensaje'
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

    @api.model
    def create(self, vals):
        """ Sobreescribe create para actualizar el saldo del artista y manejar referidos """
        transaccion = super(Transaccion, self).create(vals)

        if transaccion.tipo_transaccion == 'ingreso':
            transaccion.artista_id.saldo += transaccion.importe
        elif transaccion.tipo_transaccion == 'retiro':
            transaccion.artista_id.saldo -= transaccion.importe

            # Verificar si el mensaje comienza con '[PLAYLISTS'
            if transaccion.mensaje.startswith('[PLAYLISTS'):
                artista_referido = transaccion.artista_id.referido_por_id
                if artista_referido:
                    importe_referido = transaccion.importe * 0.15
                    mensaje_referido = f'REFERIDO ARTISTA #{transaccion.artista_id.id} TRANSACCION #{transaccion.id}'

                    self.create({
                        'artista_id': artista_referido.id,
                        'tipo_transaccion': 'ingreso',
                        'importe': importe_referido,
                        'mensaje': mensaje_referido,
                    })

        return transaccion
