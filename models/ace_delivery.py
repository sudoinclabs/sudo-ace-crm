from odoo import models, fields, api


class SudoAceDelivery(models.Model):
    _name = 'ace.delivery'
    _rec_name = 'name'

    name = fields.Char(string='Delivery Model')