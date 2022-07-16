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
        'security/ir.model.access.csv',
        'views/certificate_types_view.xml',
        'views/traffic_department_view.xml',
        'views/res_partner_view.xml',
        'views/sequence.xml',
        'views/certificate_view.xml',
        'reports/reports.xml',
        'reports/certificate_template.xml',



    ],
    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
    }