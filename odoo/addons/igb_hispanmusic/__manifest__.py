# -*- coding: utf-8 -*-
{
    'name': "HispanMusic",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "HispanMusic",
    'website': "https://hispanmusic.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
       'security/hispanmusic_security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/artista_views.xml',
        'views/cancion_views.xml',
    ],

    'installable': True,
    'application': True,
}

