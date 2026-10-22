# -*- coding: utf-8 -*-
{
    'name': 'SkynetAccessibility Scanner Pro',
    'version': '1.0.0',
    'category': 'Website',
    'summary': 'Paid plan (Small Site, 100 pages, annual). Scan, monitor, and identify website accessibility issues across WCAG 2.0, 2.1, 2.2, ADA, Section 508, EN 301 549, UK Equality Act, Australian DDA, and Canada ACA. Get simple issue highlights with recommended fixes.',
    'author': 'Skynet Technologies',
    'website': 'https://www.skynettechnologies.com',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'models/skynetpro_scanner_model.xml',
        'security/ir.access.csv',
        'views/skynetpro_scanner_views.xml',    
        'views/skynetpro_scanner_menu.xml',     
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
