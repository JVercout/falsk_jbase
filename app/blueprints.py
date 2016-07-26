"""
All Flask blueprints for the entire application.

All blueprints for all modules go here.
Blueprint URL paths are defined here.
They shall be imported by the views themselves and by application.py.
"""

from flask import Blueprint


def _factory(partial_module_string, url_prefix):
    """Generates blueprint objects for modules.

    Positional arguments:
    partial_module_string -- string representing a module without the absolute path (e.g. 'home.index' for
        app.modules.management.index).
    url_prefix -- URL prefix passed to the blueprint.

    Returns:
    Blueprint instance for a module.
    """
    name = partial_module_string
    import_name = 'app.modules.{}'.format(partial_module_string)
    template_folder = 'templates'
    blueprint = Blueprint(name, import_name, template_folder=template_folder, url_prefix=url_prefix)
    return blueprint


management_console = _factory('management.index', '/')
twilio_gateway = _factory('twilio.index', '/gateway/twilio')
clickatell_gateway = _factory('clickatell.index', '/gateway/clickatell')


all_blueprints = (management_console, twilio_gateway, clickatell_gateway)
