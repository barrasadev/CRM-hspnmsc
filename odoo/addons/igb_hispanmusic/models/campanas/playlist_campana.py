from odoo import models, fields, api

class PlaylistCampana(models.Model):
    _name = 'igb_hispanmusic.playlist_campana'
    _description = 'Campaña de Playlist'

    cancion_id = fields.Many2one(
        'igb_hispanmusic.cancion',
        string='Canción',
        required=True
    )

    artista_id = fields.Many2one(
        'igb_hispanmusic.artista',
        string='Artista',
        compute='_compute_artista_id',
        store=True
    )

    tipo_campana_id = fields.Many2one(
        'igb_hispanmusic.tipo_campana_playlist',
        string='Tipo de Campaña',
        required=True
    )

    fecha_inicio = fields.Datetime(
        string="Fecha de Inicio",
        default=fields.Datetime.now
    )

    playlists = fields.Char(string='Playlists')
    followers_playlist = fields.Char(string='Seguidores Playlists')
    cant_playlist = fields.Char(string='Cantidad de Playlists')

    followers_user = fields.Char(string='Seguidores Usuario', required=True)
    reproducciones_cancion = fields.Char(string='Reproducciones actuales', required=True)

    estado = fields.Selection(
        [('en_cola', 'En cola'),
         ('en_espera', 'En espera'),
         ('completado', 'Completado')],
        string='Estado',
        default='en_cola',
        required=True
    )

    @api.depends('cancion_id')
    def _compute_artista_id(self):
        for record in self:
            if record.cancion_id:
                artista = self.env['igb_hispanmusic.artista'].search(
                    [('canciones_ids', 'in', record.cancion_id.id)],
                    limit=1
                )
                record.artista_id = artista.id if artista else False
            else:
                record.artista_id = False
