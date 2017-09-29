# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class tickele_test(models.Model):
#     _name = 'tickele_test.tickele_test'
#	 name = fields.Char(string='Titulo', required=True,)
#     description = fields.Text('Observaciones')

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100