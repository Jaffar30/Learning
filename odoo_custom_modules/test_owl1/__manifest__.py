{
    'name': 'Test Owl1',
    'version': '17.0.0.0.0',
    'description': 'Test Owl1',
    'summary': 'Test Owl1',
    'author': '',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/dog.xml',
        
        'views/actions.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'test_owl1/static/src/components/*/*.js',
            'test_owl1/static/src/components/*/*.xml',
            'test_owl1/static/src/components/*/*.scss',
        ],
    },
}