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


from openerp import models, api, fields

class MODTPL(models.Model):
    _name = 'MODTPL'
    _description = ''

    name = fields.Char(string='Name', size=64, help='Help note')
    user_id = fields.Many2one('res.users', string='USER_ID',
                                  default=lambda self: self.env.user,
                                  readonly=False, states={'done': [('readonly', True)]})
    state = fields.Selection([
                    ('draft', 'Draft'),
                    ('cancel', 'Cancel'),
                    ('done', 'Done')
                ], string='Status', default='draft', readonly=True, required=True, copy=False, help="")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

