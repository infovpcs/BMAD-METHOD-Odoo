{
    'name': 'My Odoo Module',
    'summary': 'Short description of my Odoo module.',
    'description': """
        Long description of your Odoo module.
        Can include multiple lines and detailed information.
    """,
    'author': 'Your Name/Company',
    'website': 'https://www.yourwebsite.com',
    'category': 'Uncategorized',
    'version': '17.0.1.0.0',
    'depends': [
        'base',
        # Add other core or custom module dependencies here, e.g.,
        # 'web',
        # 'mail',
        # 'website',
    ],
    'data': [
        # Security files
        # 'security/ir.model.access.csv',
        # 'security/my_module_security.xml',

        # View files
        # 'views/my_model_views.xml',
        # 'views/my_website_page_templates.xml',
        # 'views/menuitems.xml',

        # Data files (e.g., demo data, configurations)
        # 'data/my_module_data.xml',
    ],
    'demo': [
        # 'demo/my_module_demo.xml',
    ],
    'assets': {
        # Frontend assets (JS, CSS, XML for OWL/QWeb)
        # 'web.assets_frontend': [
        #     'my_module/static/src/js/my_component.js',
        #     'my_module/static/src/xml/my_component_template.xml',
        #     'my_module/static/src/scss/my_style.scss',
        # ],
        # Backend assets
        # 'web.assets_backend': [
        #     'my_module/static/src/js/my_backend_js.js',
        #     'my_module/static/src/xml/my_backend_template.xml',
        #     'my_module/static/src/scss/my_backend_style.scss',
        # ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False, # Set to True if it's a standalone application
    'auto_install': False,
} 