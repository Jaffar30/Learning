from odoo import models, fields, api, _

class Dog(models.Model):
    _name = 'dog'
    _description = 'Dog'

    name = fields.Char(string='name')
    is_aggressive = fields.Boolean(string='Is Aggressive')
    color = fields.Char(string='color')

    




