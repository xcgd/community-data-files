# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerIndustry(models.Model):
    _inherit = "res.partner.industry"
    _order = "code"
    _rec_name = "full_name"

    name = fields.Char(index=True)
    parent_id = fields.Many2one(index=True)
    child_ids = fields.One2many(string="NACE subcategories")
    code = fields.Char(index=True)
    partner_ids = fields.One2many(
        comodel_name="res.partner", inverse_name="industry_id", string="Partners"
    )
    _sql_constraints = [("ref_code", "unique (code)", "NACE Code must be unique!")]
