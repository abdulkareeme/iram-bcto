from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = "product.product"

    is_flower = fields.Boolean("Is Flower Product?", default=False)
    flower_id = fields.Many2one("flower.flower", string="Flower")
