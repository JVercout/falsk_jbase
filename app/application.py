"""Configuration and create_app() Flask factory method"""
import os
from importlib import import_module
from flask import Flask

import app as app_root
from app.blueprints import all_blueprints
from app.extensions import celery, db

APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app_root.__file__))
TEMPLATE_FOLDER = os.path.join(APP_ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(APP_ROOT_FOLDER, 'static')


def get_config(config_class_string, yaml_files=None):
    config_module, config_class = config_class_string.rsplit('.', 1)
    config_class_object = getattr(import_module(config_module), config_class)
    config_obj = config_class_object()

    db_fmt = 'app.models.{}'
    if getattr(config_obj, 'DB_MODELS_IMPORTS', False):
        config_obj.DB_MODELS_IMPORTS = [db_fmt.format(m) for m in config_obj.DB_MODELS_IMPORTS]

    return config_obj


def create_app(config_obj, no_sql=False):
    app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)
    config_dict = dict([(k, getattr(config_obj, k)) for k in dir(config_obj) if not k.startswith('_')])
    app.config.update(config_dict)

    # Import DB models
    with app.app_context():
        for module in app.config.get('DB_MODELS_IMPORTS', list()):
            import_module(module)
    # Setup redirects and register blueprints
    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)

    # Initialize extensions/add-ons/plugins
    db.init_app(app)
    celery.init_app(app)

    # Activate middleware

    # Return the application instance.
    return app
