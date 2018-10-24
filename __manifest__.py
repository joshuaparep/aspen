# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Aspen',
    'version': '0.3',
    'summary': 'Adoption of fleet module for glory group of companies',
    'sequence': 23,
    'author': 'Joshua Parep',
    'description': """
This is a test app for study
    """,
    'category': 'Fleet',
    'website': '',
    'images': [],
    'depends': ['fleet'],
    'data': [
        "views/glory_fleet_views.xml",
        "views/glory_fleet_parts_views.xml",
        "views/glory_fleet_responsibility_views.xml",
    ],
    'demo': [],

    'qweb': [],

    'installable': True,
    'application': True,

}
