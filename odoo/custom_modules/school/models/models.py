# -*- coding: utf-8 -*-

from odoo import models,fields,api
from odoo.exceptions import UserError

class School(models.Model):
    _name = 'school.profile'
    _description = 'school profile'

    name = fields.Char()
    school_code = fields.Integer()
    school_type = fields.Selection([('public','Public'),('private','Private')])
    # students = fields.One2many('student.profile','school_id')

