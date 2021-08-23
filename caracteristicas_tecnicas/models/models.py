# -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright(c): 2018-Today Rubén Fortunato
#   License: AGPL V3
#   License URL:
#
###############################################################################

from odoo import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'

    type = fields.Selection(default='product')

    tipo = fields.Selection([
        ('compresion', 'Compresión'),
        ('torsion', 'Torsión'),
        ('traccion', 'Tracción'),
        ('alambre_de_forma', 'Alambre de Forma'),
        ('alambre_kg', 'Alambre kg')
    ], string='Tipo', default='')

    formato1 = fields.Selection([
        ('cilindrico', 'Cilíndrico'),
        ('conico', 'Cónico'),
        ('biconico', 'Bicónico'),
    ], string='Formato', default='')

    formato2 = fields.Selection([
        ('simple', 'Simple'),
        ('doble', 'Doble')
    ], string='Formato', default='')

    material = fields.Selection([
        ('sae1070', 'SAE1070'),
        ('sae1050', 'SAE1050'),
        ('sae1080', 'SAE1080'),
        ('aisi302d', 'AISI 302D'),
        ('aisi304', 'AISI 304')
    ], string='Material', default='sae1070')

    dia_alambre = fields.Float(
        string='Ø Alambre (mm)', digits=(4, 2))

    dia_interior_1 = fields.Float(
        string='Ø Interior 1 (mm)', digits=(4, 2))
    dia_interior_2 = fields.Float(
        string='Ø Interior 2 (mm)', digits=(4, 2))
    dia_interior_3 = fields.Float(
        string='Ø Interior 3 (mm)', digits=(4, 2))
    dia_exterior_1 = fields.Float(
        string='Ø Exterior 1 (mm)', digits=(4, 2))
    dia_exterior_2 = fields.Float(
        string='Ø Exterior 2 (mm)', digits=(4, 2))
    dia_exterior_3 = fields.Float(
        string='Ø Exterior 3 (mm)', digits=(4, 2))

    largo_libre = fields.Float(string='Largo Libre (mm)', digits=(4, 2))

    paso_entre_espiras = fields.Float(string='Paso (mm)', digits=(4, 2))

    espiras_activas = fields.Float(string='Espiras Activas', digits=(4, 2))

    espiras_totales = fields.Float(string='Espiras Totales', digits=(4, 2))

    extremos = fields.Selection([
        ('abierto', 'Abierto'),
        ('abierto_rectificado', 'Abierto Rectificado'),
        ('cerrado_y_escuadrado', 'Cerrado y Escuadrado'),
        ('escuadrado_y_rectificado', 'Escuadrado y Rectificado')
    ], string='Extremos', default='')

    largo_pata_1 = fields.Float(string='Largo Pata 1 (mm)', digits=(4, 2))

    largo_pata_2 = fields.Float(string='Largo Pata 2 (mm)', digits=(4, 2))

    sentido_de_giro = fields.Selection([
        ('derecho', 'Derecho'),
        ('izquierdo', 'Izquierdo')
    ], string='Sentido De Giro', default='')

    desarrollo = fields.Float(string='Desarrollo (mm)', digits=(4, 2))

    peso_material = fields.Float(string='Peso (gr)', digits=(4, 2))

    def limpiar_campos(self, vals):
        """ limpiar campos """
        vals.update({'formato1': False})
        vals.update({'formato2': False})
        vals.update({'dia_interior_1': 0.0})
        vals.update({'dia_interior_2': 0.0})
        vals.update({'dia_interior_3': 0.0})
        vals.update({'dia_exterior_1': 0.0})
        vals.update({'dia_exterior_2': 0.0})
        vals.update({'dia_exterior_3': 0.0})
        vals.update({'largo_libre': 0.0})
        vals.update({'paso_entre_espiras': 0.0})
        vals.update({'espiras_activas': 0.0})
        vals.update({'espiras_totales': 0.0})
        vals.update({'extremos': False})
        vals.update({'largo_pata_1': False})
        vals.update({'largo_pata_2': False})
        vals.update({'sentido_de_giro': False})
        return vals

    def limpiar_desarrollo(self, vals):
        """ limpiar campos """
        vals.update({'desarrollo': 0.0})
        vals.update({'peso_material': 0.0})
        return vals

    def limpiar_alambre(self, vals):
        """ limpiar campos """
        vals.update({'material': False})
        vals.update({'dia_alambre': 0.0})
        return vals

    def limpiar_datos(self, vals):
        """ limpia los valores de caracteristicas tecnicas """
        if 'tipo' in vals:
            if vals['tipo'] == 'compresion' or vals['tipo'] == 'traccion':
                vals.update({'formato2': False})
            elif vals['tipo'] == 'torsion':
                vals.update({'formato1': False})
                vals.update({'dia_interior_2': 0.0}) 
                vals.update({'dia_exterior_2': 0.0})
                vals.update({'dia_interior_3': 0.0})
                vals.update({'dia_exterior_3': 0.0})
            elif vals['tipo'] == 'alambre_de_forma':
                vals = self.limpiar_campos(vals)
            elif vals['tipo'] == 'alambre_kg':
                vals = self.limpiar_campos(vals)
                vals = self.limpiar_desarrollo(vals)
            elif vals['tipo'] is False:
                vals = self.limpiar_campos(vals)
                vals = self.limpiar_alambre(vals)
                vals = self.limpiar_desarrollo(vals)
        elif 'formato1' in vals:
            vals.update({'formato2': False})
            if vals['formato1'] == 'cilindrico':
                vals.update({'dia_interior_2': 0.0}) 
                vals.update({'dia_exterior_2': 0.0})
                vals.update({'dia_interior_3': 0.0})
                vals.update({'dia_exterior_3': 0.0})
            elif vals['formato1'] == 'conico':
                vals.update({'dia_interior_3': 0.0})
                vals.update({'dia_exterior_3': 0.0})
        elif 'formato2' in vals:
            vals.update({'formato1': False})
            vals.update({'dia_interior_2': 0.0})
            vals.update({'dia_exterior_2': 0.0})
            vals.update({'dia_interior_3': 0.0})
            vals.update({'dia_exterior_3': 0.0})

        return vals


    @api.model
    def create(self, vals):
        """ inherited create method """
        vals = self.limpiar_datos(vals)
        res = super(Product, self).create(vals)
        return res


    def write(self, vals):
        """ inherited write method """
        vals = self.limpiar_datos(vals)
        res = super(Product, self).write(vals)
        return res
