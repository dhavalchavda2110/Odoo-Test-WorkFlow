from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    tag_ids = fields.Many2many('crm.tag', string="Tags")

    def _prepare_stock_picking(self):
        res = super()._prepare_stock_picking()
        if self.sale_id:
            res['tag_ids'] = [(6, 0, self.sale_id.tag_ids.ids)]
        return res
