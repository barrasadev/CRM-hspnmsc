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
        'views/artista_views.xml',
        'views/cancion_views.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
