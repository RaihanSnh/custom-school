# -*- coding: utf-8 -*-
{
    'name': "custom_school",

    'summary': "Academy Course Module",

    'description': """
First Custom Module
    """,

    'author': "Raihan Satya Natha Hamzah",
    'website': "https://www.infinyscloud.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'School',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/course_views.xml',
        'views/templates.xml',
        'views/course_category_views.xml',
        'views/res_partner.xml',
        
        'views/session_views.xml',
        'reports/session_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}

