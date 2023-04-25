from odoo import fields, models


class MarvelCharacter(models.Model):
    _name = 'marvel.character'
    _description = 'Marvel Characters'

    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    thumbnail = fields.Char(string='Thumbnail')
