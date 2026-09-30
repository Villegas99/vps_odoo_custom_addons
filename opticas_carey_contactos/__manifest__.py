# -*- coding: utf-8 -*-
{
    'name': 'Ópticas Carey - Contactos',
    'version': '1.0.0',
    'category': 'Contacts',
    'summary': 'Registro de visitas asociadas a contactos',
    'description': """
        Extiende el modelo de contactos para registrar visitas asociadas a cada contacto.
        Incluye datos clínicos, examen visual y receta médica.
    """,
    'author': 'Aurux',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/opticas_carey_contactos_line_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}