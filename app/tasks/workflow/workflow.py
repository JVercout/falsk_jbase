""" Execute a workflow """

from flask.ext.celery import single_instance
from app.extensions import celery


@celery.task(bind=True)
@single_instance
def add(x, y):
    print('task is being proceeded', x, y)
    return x + y
