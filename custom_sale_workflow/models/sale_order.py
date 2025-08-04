from odoo import models, fields

class InheirtResPartner(models.Model):
    _inherit = "res.partner"

    reference = fields.Char(string="Reference")

    def _compute_display_name(self):
        for partner in self:
            if partner.reference:
                partner.display_name = f"{partner.name} - {partner.reference}"
            else:
                partner.display_name = partner.name       

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for do_pick in self.picking_ids:
            do_pick.write({'tag_ids': self.tag_ids.ids})
        return res

    def _send_mail_sales_person(self):
        for rec in self: 
            if record.state == 'sale' and record.origin:
                SaleOrder = env['sale.order'].sudo().search([('name', '=', record.origin)], limit=1)
                if SaleOrder and SaleOrder.user_id and SaleOrder.delivery_status in ['partial', 'full']:
                    template = self.env.ref('custom_sale_workflow.mail_template_sale_delivery_notify', raise_if_not_found=False)
                    if template:
                        print("template-----------------------")
                        template.sudo().send_mail(SaleOrder.id, force_send=True)

class ProcurementRule(models.Model):
    _inherit = 'stock.rule'

    def _run_buy(self, procurements):
        procurements_by_cat = {}
        for procurement in procurements:
            category = procurement.product_id.categ_id.id
            procurements_by_cat.setdefault(category, []).append(procurement)
        
        for category_id, procs in procurements_by_cat.items():
            super(ProcurementRule, self)._run_buy(procs)  # Run separate POs per category

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def write(self, vals):
        for record in self:
            if (
                'product_qty' in vals
                and record.state not in ['draft', 'cancel']
                and record.origin  # only if created from a sale order
            ):
                raise exceptions.UserError("You cannot change the quantity after confirmation for MOs created from a sale order.")
        return super(MrpProduction, self).write(vals)