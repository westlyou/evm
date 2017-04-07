# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Lista de indicadores posibles asociados a un proyecto

_TIPO_INDICADOR = [('PV', 'Valor planificado (Planned Value)'),
                   ('EV', 'Valor ganado (Earned Value)'),
                   ('AC', 'Coste real (Actual Cost)'),
                   ('CV', 'Variación de coste (Cost Variance)'),
                   ('CVP', 'Variación del coste (Cost Variance Percent)'),
                   ('CPI', 'Índice de desempeño del coste (Cost Performance Index)'),
                   ('TCPI', 'Índice de desempeño del trabajo por completar (To-Complete Cost Performance Index)'),
                   ('SV', 'Variación de tiempo (Schedule Variance)'),
                   ('SVP', 'Variación del cronograma (Schedule Variance Percent)'),
                   ('SPI', 'Índice de desempeño del cronograma (Schedule Performance Indexs)'),
                   ('EAC', 'Estimación a la conclusión (Estimate at Completion)'), 
                   ('ETC', 'Estimación hasta la conclusión (Estimate to Complete)'),
                   ('VAC', 'Variance at Completion'),
                   ('VACP', 'Variance at Completion Percent'),
                   ('BAC', 'Presupuesto a la conclusion (Budget at Completion)'),
                   ('PCC', 'Costs to date / Total costs'),
                   ('POC', '% Complete')]

################################################################################
#
# Indicadores asociados al proyecto
#
################################################################################
class project_evm(models.Model):
    _name = 'project.evm'
    _description = 'Indicadores para controlar el valor ganado de los proyectos'
    _inherit = ['mail.thread']

    name = fields.Char('Descripción', required=True, copy=False, help='Nombre del proceso que ha generado el indicador')
    project_id = fields.Many2one('project.project', string='Proyecto', required=True, help='Proyecto al cual esta asociado el indicador')
    tipo_indicador = fields.Selection(_TIPO_INDICADOR, 'Tipo', required=True, help='Tipo de indicador EVM')
    valor_indicador = fields.Float('Valor', copy=False, help='Valor del indicador EVM')
    fecha_registro = fields.Date('', required=True, help='Fecha de registro del indicador')
    observaciones = fields.Text('Observaciones', copy=False, help='Comentarios de interes acerca de la anotación del valor del indicador')
