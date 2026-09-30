# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_occupation = fields.Char(string='Ocupación')
    x_age = fields.Integer(string='Edad')
    x_visits_1 = fields.One2many(
        comodel_name='x_res_partner_line',
        inverse_name='x_res_partner_id',
        string='Visitas',
    )
    x_pathological_history_general = fields.Text(string='APG (Antecedentes Patológicos Generales)')
    x_pathological_history_ocular = fields.Text(string='APO (Antecedentes Patológicos Oculares)')
    x_allergies = fields.Text(string='Alergias')
    x_difficulty_distance_near = fields.Char(string='Dificultad lejos/cerca')
    x_used_glasses_before = fields.Boolean(string='¿Ha usado anteojos?')