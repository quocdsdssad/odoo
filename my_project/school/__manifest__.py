{

    'name': 'My Odoo',

    'version': '1234',

    'summary': 'My Odoo',

    'category': 'Tools',

    'author': 'Niyas Raphy',

    'maintainer': 'My Odoo',

    'company': 'My Odoo',

    'website': 'https://www.cybrosys.com',

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/student_plus_view.xml',
        'security/student_right.xml',
        'views/lang_views.xml',
        'views/test_email.xml',
    ],

    'images': [],

    'license': 'AGPL-3',

    'installable': True,

    'application': False,

    'auto_install': False,
}
