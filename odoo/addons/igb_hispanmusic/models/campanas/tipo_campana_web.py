from odoo import models, fields

class TipoCampanaWeb(models.Model):
    _name = 'igb_hispanmusic.tipo_campana_web'
    _description = 'Tipo de Campaña Página Web'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    imagen = fields.Image(string="Imagen")
    precio = fields.Float(string="Precio", required=True, digits=(10,2))
    coste = fields.Float(string="Coste", required=True, digits=(10,2))
    plantilla = fields.Char(string="Plantilla (URL)")
