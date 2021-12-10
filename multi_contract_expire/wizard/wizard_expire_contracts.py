# coding: utf-8
from odoo import api, fields, models, tools, _
from odoo.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)

EXP_REASONS_SEL = [('1', 'Renuncia'),
                   ('4', u'Defunción'),
                   ('5', 'Abandono de labores'),
                   ('6', 'Incapacidad total o permanente'),
                   ('11', u'Inhabilitación'),
                   ('12', u'Destitución e Inhabilitación'),
                   ('27', u'Conclusión de contrato'),
                   ('29', u'Liquidación'),
                   ('33', 'Licencia sin goce de sueldo')]


class WizardExpireContractsMulti(models.TransientModel):
    _name = 'wizard.expire.contracts.multi'
    _description = "Expire Contracts Wizard"

    contract_ids = fields.Many2many('hr.contract', 'bajas_wizard_contract',
                                    'wizard_id', 'contract_id', string='Contratos')
    date_end = fields.Date('Fecha de baja')
    expired = fields.Boolean('Expirado', default=False,
                             help='Marca el Contrato como expirado.')
    expiration_reason = fields.Selection(EXP_REASONS_SEL, string='Motivo de baja')
    state = fields.Selection([('init', 'Inicio'), ('end', 'Finalizado')], string='Estado', default='init')

    def show_wizard(self):
        return {
            'name': 'Generar Bajas de Empleados',
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'views': [(False, 'form')],
            'target': 'new'
        }

    def _reopen_wizard(self):
        return {
            'name': _('Bajas de Empleados'),
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'target': 'new',
            'view_mode': 'form'
        }

    def generate_expirations(self):
        if len(self.contract_ids) == 0:
            msg = _(u"Debe seleccionar algún Contrato antes de generar una baja!")
            raise Warning(msg)

        for contract in self.contract_ids:
            values = {
                'date_end': self.date_end,
                'expiration_reason': self.expiration_reason,
            }
            if self.expired:
                values.update({'state': 'close'})

            contract.write(values)

        self.state = 'end'
        return self._reopen_wizard()
