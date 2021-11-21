'''
Copyright ©2021 RMF
'''

from odoo import models, fields, api, _

class sale_order(models.Model):
    '''
    Reemplaza el informe de orden de venta en el botón print
    '''
    _inherit = 'sale.order'

    def print_quotation(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        return self.env.ref('reportes_modernos.sale_order_report').report_action(self)
