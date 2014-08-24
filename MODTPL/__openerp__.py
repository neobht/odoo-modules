# -*- coding: utf-8 -*-
##############################################################################
#
#    MODTPL module for OpenERP,
#    Copyright (C) 20xx SibSAU UIT Projects (<http://www.sibsau.ru>)
#    Anton Goroshkin (neobht@sibsau.ru)
#
#    This file is a part of MODTPL
#
#    MODTPL is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MODTPL is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'MODTPL',
    'version': '1.0',
    'category': 'Tools',
    'description': """
The common interface and structure for modules.
=================================
""",
    'author': 'Anton Goroshkin',
    'website': 'http://www.sibsau.ru',
    'depends': ['base'],
    'data': [
        'views/MODTPL_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
