"""
Template for a new Odoo model.

This template provides a basic structure for an Odoo model, including common fields,
docstrings, and an example of a simple method. It aims to adhere to Odoo 17/18
best practices for model definition.
"""

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'Description of My Model'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Optional: Add chatter and activities

    name = fields.Char(string='Name', required=True, help='A unique name for this record.')
    active = fields.Boolean(string='Active', default=True, help='Set to false to hide the record instead of deleting it.')
    description = fields.Text(string='Description', help='Detailed description of the record.')
    value = fields.Float(string='Value', digits=(16, 2), help='A numerical value.')
    date_field = fields.Date(string='Date Field', help='A date field.')
    datetime_field = fields.Datetime(string='Datetime Field', help='A datetime field.')
    # Example of a many2one field
    partner_id = fields.Many2one('res.partner', string='Partner', help='Associated partner for this record.')
    # Example of a one2many field (add 'my_model_id' to res.partner for this to work)
    # partner_ids = fields.One2many('res.partner', 'my_model_id', string='Partners')

    @api.constrains('name')
    def _check_name_unique(self):
        """
        Constraint to ensure the name is unique across all active records.
        """
        for record in self:
            if self.search([('name', '=', record.name), ('id', '!=', record.id), ('active', '=', True)]):
                raise ValidationError(_("The name '%s' must be unique!") % record.name)

    @api.depends('value')
    def _compute_display_name(self):
        """
        Compute method for display name.
        """
        for record in self:
            record.display_name = f"{record.name} ({record.value})"

    def do_something(self):
        """
        A sample method demonstrating an action.
        """
        self.ensure_one()
        # Add your logic here
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Action completed successfully!',
                'type': 'rainbow_man',
            }
        }

    # Example of a SQL constraint
    # _sql_constraints = [
    #     ('name_unique',
    #      'UNIQUE(name)',
    #      'The name must be unique !'),
    # ] 