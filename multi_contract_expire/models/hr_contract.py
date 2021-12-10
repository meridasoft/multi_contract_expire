# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.addons.multi_contract_expire.wizard.wizard_expire_contracts import EXP_REASONS_SEL
import logging

_logger = logging.getLogger(__name__)


class ContractInherit(models.Model):
    _inherit = 'hr.contract'

    expiration_reason = fields.Selection(EXP_REASONS_SEL, string='Motivo de baja')
            
    def write(self, vals):
        if 'state' in vals and vals.get('state') == 'close' and 'expiration_reason' not in vals:
            for record in self:
                if not record.expiration_reason:
                    # End contract
                    vals['expiration_reason'] = '27'

        res = super(ContractInherit, self).write(vals)

        # create history record after expired the contract
        if 'state' in vals and vals.get('state') == 'close':
            for record in self:
                history_id = self.env['history.expired.contract'].search([('contract_id', '=', record.id)], limit=1)
                if not history_id:
                    self.env['history.expired.contract'].create({'contract_id': record.id})
                # redefine end date of the contract (past, present or future)
                if 'date_end' in vals:
                    record.write({'date_end': vals.get('date_end')})
        return res
