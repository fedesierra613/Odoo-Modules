{
    'name': 'custom_apimarvel',
    'version': '1.0',
    'summary': 'Modulo de pruebas para consumir APIs',
    'description': 'Se relaizaran pruebas para consumir APIs desde Odoo',
    'author': 'Federico Sierra',
    'depends': ['Base'],
    'application': True,
    'data': [
        'views/mi_vista.xml',
        'models/example_api.py',
    ],
	
    'installable': True,
}
