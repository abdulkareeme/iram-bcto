from odoo import models,api,fields


class Flower(models.Model):
    _name = 'flower.shop'
    _description = 'Flower'

    name = fields.Char(string='Common Name', required=True)
    scientific_name = fields.Char(string='Scientific Name')
    season_start = fields.Date(string='Season Start')
    season_end = fields.Date(string='Season End')
    watering_frequency = fields.Integer(string='Watering Frequency (days)', help='Frequency is in number of days')
    watering_amount = fields.Integer(string='Watering Amount (ml)')

