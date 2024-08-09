{
    'name': 'Flower Shop',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage flowers in a flower shop',
    'description': 'A module to manage flowers, including their attributes and watering schedule.',
    'author': 'Eng:Lubna Alabdah',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/flower_views.xml',
        'views/flower_products.xml',
    ],
    'installable': True,
    'application': True,
}
