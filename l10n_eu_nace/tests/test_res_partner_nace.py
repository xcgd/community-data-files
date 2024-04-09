# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestResPartnerNace(TransactionCase):
    def setUp(self):
        super(TestResPartnerNace, self).setUp()
        self.nace = self.env["res.partner.industry"].create(
            {"name": "nace_test", "code": "code_nace"}
        )
        self.child_nace = self.env["res.partner.industry"].create(
            {
                "name": "nace_child",
                "code": "code_child",
                "parent_id": self.nace.id,
            }
        )
        self.child_copy = self.child_nace.copy()

    def test_01_check_copy(self):
        self.assertEqual(self.child_copy.name, "nace_child 2")

    def test_02_check_uniq_code(self):
        self.assertNotEqual(self.child_copy.code, self.child_nace.code)
