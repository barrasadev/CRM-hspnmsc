# Author: Ivan Gonzalez Barrasa (barrasa.dev)
# File: __manifest__.py
# Path: ~/Proyectos/HispanMusic/CRM-hspnmsc/odoo/addons/igb_hispanmusic
# Created: 2025-02-14 15:52
# Last Updated: 2025-02-14 15:52

{
    'name': "HispanMusic",
    'summary': "Gestión de artistas musicales",
    'description': "Módulo para la gestión de artistas musicales y sus canciones",
    'author': "HispanMusic",
    'website': "https://hispanmusic.com",
    'category': 'Music',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/hispanmusic_security.xml',
        'views/artistas/artista_views.xml',
        'views/artistas/cancion_views.xml',
        'views/campanas/tipo_campana_playlist_views.xml',
        'views/campanas/tipo_campana_web_views.xml',
        'views/campanas/playlist_campana.xml',
        'views/artistas/transaccion_views.xml',
        'views/artistas/menu.xml',
        'views/campanas/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
