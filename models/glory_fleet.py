# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _

#This class inherit the fleet module and changes the views from inherited field.
class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    #two test fielda added on the inherited form view
    myfuel_gallon = fields.Integer("My Fuel in Galoon", default=200)
    myresult = fields.Integer(string='In Litters', compute='convert_gallon_to_litter', readonly='True')

    #conversts gallons to litters
    def convert_gallon_to_litter(self):
        for line in self:
            line.myresult = self.myfuel_gallon * 3.78541

    #test for onchange method
    @api.onchange('seats', 'doors', 'color')
    def onchange_internal_type(self):
        if self.seats == 1 or self.doors == 4 or self.color == 'red':
            self.myfuel_gallon = 50

#class for the vehicle parts
class FleetVehicleParts(models.Model):
    _name = 'fleet.vehicle.parts'
    _description = 'Spare Parts of a vehicle'

    #sample fields added
    parts_name = fields.Char('Parts Name')
    parts_location = fields.Many2one('res.country', 'Parts Location')
    parts_unit = fields.Integer('Parts Unit', default=0)
    parts_stock = fields.Date('Date')

#class for accontability and responsibility model
class FleetVehicleResponsibility(models.Model):
    _name = 'fleet.vehicle.responsibility'
    _description = 'Responsibility of a vehicle'

    #sample fields added
    vehicle_respons = fields.Char(string='Responsibility  Name')
    action_list = fields.Char(string='Action List')
    task_complete = fields.Integer(string='Task Complete', default=0)
    task_incomplete = fields.Integer(string='Task Incomplete', default=0)