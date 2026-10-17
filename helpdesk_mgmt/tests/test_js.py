# Copyright 2025 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestHelpdesMgmtJs(HttpCase):
    def test_helpdesk_mgmt(self):
        self.browser_js(
            '/web/tests?headless&loglevel=2&preset=desktop&filter="@helpdesk_mgmt"',
            "",
            login="admin",
            timeout=600,
            success_signal="[HOOT] Test suite succeeded",
        )
