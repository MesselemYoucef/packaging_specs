from odoo import models, fields, api


class ProductTemp(models.Model):
    _inherit = 'product.template'

    pcs_per_cartoon = fields.Integer(string="Pieces per Carton")
