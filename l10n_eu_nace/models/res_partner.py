# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    industry_id = fields.Many2one(string="Main NACE", index=True)
    secondary_industry_ids = fields.Many2many(string="Secondary NACE")
