# -*- coding: utf-8 -*-
from odoo import models, fields


class OpticasCareyContactosLine(models.Model):
    _name = 'x_res_partner_line'
    _description = 'Visita de contacto'
    _order = 'create_date desc'
    _rec_name = 'x_clinical_history'

    x_res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Paciente',
        required=True,
        ondelete='cascade',
        index=True,
    )

    x_clinical_history = fields.Text(string='Historia Clínica')
    x_light_sensitivity = fields.Boolean(string='¿Molesta luz solar o artificial?')
    x_last_prescription_date = fields.Date(string='Fecha última graduación')
    x_previous_prescription = fields.Char(string='RX Anterior')

    # Examen Visual
    x_av_ca = fields.Char(string='Agudeza Visual Con Anteojos (AV C/A)')
    x_av_sa = fields.Char(string='Agudeza Visual Sin Anteojos (AV S/A)')
    x_di = fields.Char(string='DI')

    # Receta Médica
    x_rx = fields.Char(string='RX')
    x_od = fields.Float(string='Ojo Derecho (OD)')
    x_oi = fields.Float(string='Ojo Izquierdo (OI)')
    x_add = fields.Float(string='ADD (Adición)')
    x_optometistra = fields.Many2one(
        comodel_name='res.partner',
        string='Optometrista',
    )