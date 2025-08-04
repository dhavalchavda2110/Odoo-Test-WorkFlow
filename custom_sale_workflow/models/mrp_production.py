from odoo import models, fields, api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.onchange('product_qty')
    def _check_change_qty(self):
        if self.state != 'draft':
            raise UserError("You can't change the quantity after confirmation.")
