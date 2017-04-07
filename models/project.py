# -*- coding: utf-8 -*-

from odoo import models, fields, api

################################################################################
#
# Project Tasks
#
################################################################################
class Task(models.Model):
	_inherit = 'project.task'

	date_expectedstart = fields.Date(string='Expected start date', index=True, help='Expected start date')
