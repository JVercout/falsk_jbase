from flask import Flask
from app.application import get_config, create_app


def test_get_config():
    config = get_config('app.config.Testing')

    assert config.TESTING is True


def test_create_app():
    app = create_app(get_config('app.config.Testing'))

    assert isinstance(app, Flask) is True
