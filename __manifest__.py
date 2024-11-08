# -*- coding: utf-8 -*-
{
    'name': "Filmoteca (ErikAT)",

    'summary': """
        Pruebas de Python""",

    'description': """
        No hay descripción larga
    """,

    'author': "ErikAT",
    'website': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/pelicula.xml',
        'views/genero.xml',
        'views/tecnica.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
