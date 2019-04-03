# -*- coding: utf-8 -*-
{
    'name': "El Barrio - Registro Clientes",

    'summary': """
        En este módulo registraremos los distintos clientes de El Barrio""",

    'description': """
        Esto es descripción
    """,

    'author': "El Barrrio",
    'website': "http://www.elbarrio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'El Barrio-Registro',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'muk_web_theme'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/registro_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True
}