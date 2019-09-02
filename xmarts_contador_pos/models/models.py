# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import datetime
import time




class posQuantFilter(models.TransientModel):
    _name = 'pos.order.filter'
    _description = 'Valoración de Inventario con Filtros'

    compute_at_date = fields.Selection([
        (0, 'Mostrar todo el inventario'),
        (1, 'Filtrar por fecha')
    ], string="Compute", help="Muestra con filtros el inventario")
    date = fields.Date('Inventory at Date', help="Choose a date to get the inventory at that date")
    idate = fields.Date('Inventory Start Date', help="Choose a date")

    def open_table(self):
        self.ensure_one()        
 
        if self.compute_at_date:
            tree_view_id = self.env.ref('xmarts_contador_pos.view_pos_order_tree_all_sales_lines_stock').id   
            # We pass `to_date` in the context so that `qty_available` will be computed across
            # moves until date.
            action = {
                'type': 'ir.actions.act_window',
                'views': [(tree_view_id, 'tree')],
                'view_mode': 'tree,form',
                'name': _('Inventario Rotativo'),
                'res_model': 'pos.order.line',
                'context':{'fecha_inicio':self.idate,'fecha_final':self.date, 'group_by':'product_id'},
                'domain':  ['&',('create_date', '<=',  self.date),('create_date', '>=',  self.idate)],
            }
            return action
        else:
            tree_view_id = self.env.ref('xmarts_contador_pos.view_pos_order_tree_all_sales_lines_stock').id   
            # We pass `to_date` in the context so that `qty_available` will be computed across
            # moves until date.
            action = {
                'type': 'ir.actions.act_window',
                'views': [(tree_view_id, 'tree')],
                'view_mode': 'tree,form',
                'name': _('Inventario Rotativo'),
                'res_model': 'pos.order.line',
                #"'context': dict(self.env.context, to_date=self.date),
                'context':{'group_by':'product_id'},
                'domain':  [],
            }
            return action
        
   

class pos_order_line(models.Model):

    _inherit ='pos.order.line'

    laundry_state_related = fields.Selection([('pendiente','Pendiente'),('proceso','En proceso'),('terminado','Listo Para Entrega'),('entregado','Entregado')], related='order_id.laundry_state', string="Estado de prendas")
    estado_fila = fields.Float(
        string='Inventario',compute='_compute_peso',store=True
    )

    @api.one
    @api.depends('laundry_state_related')
    def _compute_peso(self):
        for x in self:
            if x.laundry_state_related == "entregado":
                x.estado_fila = x.qty * 0
            else:
                x.estado_fila = x.qty *1