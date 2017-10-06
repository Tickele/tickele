# -*- coding: utf-8 -*-
{
    'name': "Tickele",
    'summary': """
        Odoo 10""",
    'description': """
        Modulo para integrar Tickele con Odoo.
		Con Tickele podras enviar a tus usuarios los tickets y facturas sin necesidad de imprimilos. Ademas, tambien podras enviar promociones especiales para fidelizarlos.
		Para mas información visita https://tickele.com/
    """,
	'sequence': 6,
    'author': "Tickele",
    'website': "http://www.tickele.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
	
	'images': ['images/main-screenshot.png'],
	

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
		'views/tickele_test.xml',
    ],
	'installable': True,
    'auto_install': False,
}
