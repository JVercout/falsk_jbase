"""
Flask Extensions instantiated here.

To avoid circular imports with views and create_app(), extensions are instantiated here.
They will be initialized (calling init_app()) in application.py.
"""

from flask.ext.celery import Celery
from app.models.history_meta import versioned_session
from flask.ext.sqlalchemy import SQLAlchemy, SignallingSession

versioned_session(SignallingSession)
db = SQLAlchemy()
celery = Celery()
