from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = 'product.category'

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Category name must be unique!')
    ]
