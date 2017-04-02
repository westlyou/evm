# -*- coding: utf-8 -*-

from odoo import models, fields, api

class project_evm(models.Model):
    _name = 'project.evm'

    name = fields.Char()
    description = fields.Text()
