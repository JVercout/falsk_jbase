#!/usr/bin/env python
"""
Flaskr Application Framework

Usage:
    manage.py devserver [-p NUM]
    manage.py celerydev
    manage.py create_all
    manage.py (-h | --help)

Options:
    -p NUM --port=NUM           Flask will listen on this port number
                                [default: 5000]
"""

import signal
import sys

from functools import wraps
from docopt import docopt

from celery.bin.celery import main as celery_main
from app.application import create_app, get_config
from app.extensions import db

OPTIONS = docopt(__doc__) if __name__ == '__main__' else dict()


def command(func):
    """Decorator that registers the chosen command/function.
    If a function is decorated with @command but that function name is not a valid "command" according to the docstring,
    a KeyError will be raised, since that's a bug in this script.
    If a user doesn't specify a valid command in their command line arguments, the above docopt(__doc__) line will print
    a short summary and call sys.exit() and stop up there.
    If a user specifies a valid command, but for some reason the developer did not register it, an AttributeError will
    raise, since it is a bug in this script.
    Finally, if a user specifies a valid command and it is registered with @command below, then that command is "chosen"
    by this decorator function, and set as the attribute `chosen`. It is then executed below in
    `if __name__ == '__main__':`.
    Doing this instead of using Flask-Script.
    Positional arguments:
    func -- the function to decorate
    """
    @wraps(func)
    def wrapped():
        return func()

    # Register chosen function.
    if func.__name__ not in OPTIONS:
        raise KeyError('Cannot register {}, not mentioned in docstring/docopt.'.format(func.__name__))
    if OPTIONS[func.__name__]:
        command.chosen = func

    return wrapped

# # TODO: Load app.config.Config by default, or Test/production config on demand
# # TODO: Launch in production behing NginX with gunicorn/tornado?


@command
def devserver():
    app = create_app(get_config('app.config.Config'))
    app.run()


@command
def celerydev():
    app = create_app(get_config('app.config.Config'))
    celery_args = ['celery', 'worker', '-B', '-s', '/tmp/celery.db', '--concurrency=5']
    with app.app_context():
        return celery_main(celery_args)


@command
def create_all():
    app = create_app(get_config('app.config.Config'))
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))  # Properly handle Control+C
    if not OPTIONS['--port'].isdigit():
        print('ERROR: Port should be a number.')
        sys.exit(1)
    getattr(command, 'chosen')()  # Execute the function specified by the user.
    # manager.run()
