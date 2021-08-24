{
    'name': "Calculator",
    'version': '1.0',
    'author': "Odoo",
    'category': 'Addition',
    'depends': ['website'],
    # data files always loaded at installation
    'data': [
        'views/addition.xml',
        'views/template.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
