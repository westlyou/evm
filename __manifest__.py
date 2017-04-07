# -*- coding: utf-8 -*-
{
    'name': "EVM",

    'summary': """
        Gestión del valor ganado para controlar la ejecución 
        de un proyecto""",

    'description': """
        Según Wikipedia (http://es.wikipedia.org), la Gestión del Valor Ganado es una técnica de gestión de proyectos 
        que permite controlar la ejecución de un proyecto a través de su presupuesto y de su calendario de ejecución.

        Compara la cantidad de trabajo ya completada en un momento dado con la estimación realizada antes del comienzo 
        del proyecto. De este modo, se tiene una medida de cuánto trabajo se ha realizado, cuanto queda para finalizar 
        el proyecto y extrapolando a partir del esfuerzo invertido en el proyecto, el Project Manager puede estimar 
        los recursos que se emplearán para finalizar el proyecto. Con esta metodología se puede estimar en cuanto 
        tiempo se completaría el proyecto si se mantienen las condiciones con las que se elaboró el cronograma o 
        considerando si se mantienen las condiciones que se presentaron durante el desarrollo del proyecto. 
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv'
        'views/project.xml',
        'views/project_evm.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/project_ev_demo.xml',
    ],
}