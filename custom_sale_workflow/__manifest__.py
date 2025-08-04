{
    'name': 'Custom Sale Workflow Enhancements',
    'version': '17.0.1.0.0',
    'summary': 'Enhancements for Sales, Delivery, MRP, and Purchase workflows',
    'author': 'Dhaval Chavda',
    'depends': ['sale', 'stock', 'purchase', 'mrp'],
    'data': [
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
        'views/res_partner_view.xml',
        'views/res_category_view.xml',
        'data/mail_action.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_sale_workflow/static/src/js/copy_clipboard.js',
        ]
    },
    'installable': True,
    'application': False,
}
