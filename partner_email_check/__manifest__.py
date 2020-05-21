# Copyright 2019 Komit <https://komit-consulting.com>
# Copyright 2020 JCMontoya <https://odooerpcloud.com> (MIG 13.0)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Email Format Checker',
    'version': '12.0.2.0.1',
    'summary': 'Validate email address field',
    'author': "Komit, Odoo Community Association (OCA), Juan Carlos Montoya",
    'website': 'https://github.com/OCA/partner-contact',
    'category': 'Tools',
    'depends': ['base_setup'],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': ['email_validator']
    },
    'data': [
        'views/base_config_view.xml',
    ]
}
