from odoo import models, fields, api


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    @api.depends('stage_id')
    def _compute_close_rate(self):
        """Calcula probability basado en la etapa y actualiza ambos campos"""
        stage_rates = {
            'Generar Interés': 0,
            'Interesado': 10,
            'Reunión consultiva': 20,
            'Oportunidad precalificada': 30,
            'Oportunidad calificada': 60,
            'Fortalecimiento': 80,
            'Proceso de cierre': 90,
            'Cerrado': 100,
        }
        
        for lead in self:
            if lead.stage_id and lead.stage_id.name in stage_rates:
                probability_value = stage_rates[lead.stage_id.name]
                # Actualizar ambos campos
                lead.probability = probability_value
                lead.close_rate = probability_value
            else:
                lead.probability = 0
                lead.close_rate = 0

    # Mantenemos close_rate como campo calculado/store para forzar la actualización
    close_rate = fields.Float(
        string='Porcentaje de cierre',
        compute='_compute_close_rate',
        store=True,
        readonly=False,
        help='Porcentaje de probabilidad de cierre basado en la etapa'
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Sobreescribe create para establecer probability inicial"""
        records = super().create(vals_list)
        records._compute_close_rate()
        return records

    def write(self, vals):
        """Sobreescribe write para forzar actualización de probability"""
        result = super().write(vals)
        if 'stage_id' in vals:
            self._compute_close_rate()
        return result