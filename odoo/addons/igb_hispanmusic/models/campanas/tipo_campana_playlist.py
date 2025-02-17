from odoo import models, fields

class TipoCampanaPlaylist(models.Model):
    _name = 'igb_hispanmusic.tipo_campana_playlist'
    _description = 'Tipo de Campaña Playlist'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    precio = fields.Float(string="Precio", required=True, digits=(10,2))
    coste = fields.Float(string="Coste", required=True, digits=(10,2))
    seguidores = fields.Integer(string="Seguidores estimados")
    reproducciones = fields.Integer(string="Reproducciones estimadas")
