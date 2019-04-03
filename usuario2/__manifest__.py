# -*- coding: utf-8 -*-
{
    'name': "Registro de usuario",

    'summary': """
        Modulo para registrar usuario""",

    'description': """
        Tarea de industria, creación de un modulo
    """,
    'author': "Ahora si",
    'website': "http://www.ELBarrio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}