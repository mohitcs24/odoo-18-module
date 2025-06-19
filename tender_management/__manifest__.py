{
    'name': 'Tender Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage e-tenders, documents, and bidding process',
    'author': 'Mohit',
    'depends': ['base', 'sale','mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/tender_project_views.xml',
        'views/document_type_views.xml',
    ],
    'installable': True,
    'application': True,
}