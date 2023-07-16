"""InvenHost integration plugin."""

from plugin import InvenTreePlugin
# from plugin.mixins import SettingsMixin
# from django.utils.translation import gettext_lazy as _


class InvenHostCore(InvenTreePlugin):
    """InvenHost integration plugin."""

    NAME = 'InvenHostCore'
    SLUG = 'invenhost-core'
    TITLE = "InvenHost Core"

    def your_function_here(self):
        """Do something."""
        pass
