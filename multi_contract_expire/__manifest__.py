# -*- coding: utf-8 -*-
{
    'name': "Multi Contract Expire by Meridasoft",
    'version': '13.0',
    'license ': 'LGPL-3',
    'depends': [
        'hr',
        'hr_contract',
    ],
    'category': 'HR',
    'author': "Merida Soft",
    'website': "http://www.meridasoft.com",
    'summary': """
        Adds wizard for expire multiple contracts at once.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_views.xml',
        'views/history_expired_contract_views.xml',
        'wizard/wizard_expire_contracts_view.xml',
        'views/menus.xml',
    ],
    'images': ['static/description/history.png',
               ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

