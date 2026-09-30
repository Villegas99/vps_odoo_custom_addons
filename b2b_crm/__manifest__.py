{
    'name': 'B2B CRM Lead Stage Rate',
    'version': '1.0.0',
    'category': 'CRM',
    'summary': 'Añade campo de tasa de cierre y actualización automática por etapa',
    'description': """
        Módulo que añade un campo close_rate al modelo crm.lead y
        lo actualiza automáticamente al cambiar de etapa.
    """,
    'author': 'Aurux',
    'website': 'https://www.yourcompany.com',
    'depends': ['crm'],
    'data': [
        'views/b2b_crm.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}