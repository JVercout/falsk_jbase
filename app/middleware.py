"""
Flask middleware definitions.
"""

from celery.signals import worker_process_init
from flask import current_app, request
from app.extensions import db


# Fix Flask-SQLAlchemy and Celery incompatibilities.
@worker_process_init.connect
def celery_worker_init_db(**_):
    """Initialize SQLAlchemy right after the Celery worker process forks.

    This ensures each Celery worker has its own dedicated connection to the MySQL database. Otherwise
    one worker may close the connection while another worker is using it, raising exceptions.

    Without this, the existing session to the MySQL server is cloned to all Celery workers, so they
    all share a single session. A SQLAlchemy session is not thread/concurrency-safe, causing weird
    exceptions to be raised by workers.

    Based on http://stackoverflow.com/a/14146403/1198943
    """
    # LOG.debug('Initializing SQLAlchemy for PID {}.'.format(os.getpid()))
    db.init_app(current_app)
