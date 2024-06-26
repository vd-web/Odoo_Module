# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Volodymyr Dotsenko",
    'website': "https://github.com/vd-web",
    'category': 'Tools',
    'version': '14.0.1.4',
    'depends': ['base', 'mail', 'digest'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'views/digest_views.xml',
        'data/mail_template.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not used in this example)
    # 'demo': [
    #     'data/demo.xml'
    # ],
}
