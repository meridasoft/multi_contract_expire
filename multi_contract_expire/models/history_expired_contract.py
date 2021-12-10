# -*- coding:utf-8 -*-
from odoo import fields, models, api


class HistoryExpiredContract(models.Model):
    _name = 'history.expired.contract'
    _description = "Expired Contracts History"

    contract_id = fields.Many2one('hr.contract',  string='Contrato', required='True')
    date_start = fields.Date('Fecha Inicio', related='contract_id.date_start')
    date_end = fields.Date('Fecha Final', related='contract_id.date_end')
    contract_state = fields.Selection(related='contract_id.state', string='Estado Contrato')
    expiration_reason = fields.Selection(related='contract_id.expiration_reason')
    employee_id = fields.Many2one(related='contract_id.employee_id', string='Empleado')
    employee_state = fields.Boolean(related='employee_id.active', string='Estado Empleado')
