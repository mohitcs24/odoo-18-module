{
    'name': 'Student Management',
    'version': '1.0',
    'author': 'mohit kumar',
    'depends': ['base','sale'],
    'category': 'Education',
    'description': 'Manage students',
    'data': [
        'security/ir.model.access.csv',
        'report/report.xml', 
        'report/student_report_template.xml',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True,
}

