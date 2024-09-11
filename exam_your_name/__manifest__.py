# -*- coding: utf-8 -*-
{
    'name': "Exam Your Name",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
    Exam Your Name
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','purchase','account','project','stock','sale',],

    # always loaded
    'data': [
        'security/security_veiw.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/exam_view.xml',
        'views/exam_type.xml',
        'views/student_evaluation_view.xml',
        'views/account_move_view.xml',
        'views/peoduct_template_view.xml',
        'views/project_task_view.xml',
        'views/stock_picking_view.xml',
        'views/sale_order_view.xml',
        'report/report.xml',
        'report/exam_report.xml',




    ],
    'demo': [
        'demo/exam_type_data.xml'
    ],
    'installable': True,
    'auto_install': False,
     'License': 'LGPL-3',
    'application': True,
    'sequence': -110,
}
