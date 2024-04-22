# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _


_logger = logging.getLogger(__name__)


class Estate_property(models.Model):
    _name = 'estate_property'
    _description = "Estate Property"
   
    
    name = fields.Char(_('Name'), required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date("Available from")
    expected_price = fields.Float(string="Expected Prices", required=True)
    selling_price = fields.Float(string="Selling prices", readonly=True)
    bedrooms = fields.Integer(string="Bedrooms", default="2")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facade")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([('n', 'North'), ('s', 'South'), ('e', 'East'), ('w', 'West')], string="Garden Orientation", default="n" )
    total_area = fields.Integer(string='Total Area' , 
                                    compute='_compute_total_area')
    
  # fields compute
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
   # uso del onchange 
    @api.onchange('garden')
    def _onchange_is_garden(self):        
        self.garden_area = '10'
        self.garden_orientation = "n"
        
    
    
    

    
    
    