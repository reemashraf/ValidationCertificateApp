{
    'name': "Certificate App",
    'version': '1.0',
    'depends': ['base','sale'],
    'author': "Reem",
    'description': """
    Validation Certificates App Module
    """,
    'data': [
        'views/certificate_groups.xml',
        'views/certificate_types_view.xml',
        'views/traffic_department_view.xml',
        'views/res_partner_view.xml'



    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    }