from urllib.parse import urlparse


class HardCoded(object):
    """Constants used throughout the application.

    All hard coded settings/data that are not actual/official configuration options for Flask, Celery, or their
    extensions goes here.
    """
    ADMINS = ['me@me.test']
    DB_MODELS_IMPORTS = ('user', 'watch',)  # Like CELERY_IMPORTS in CeleryConfig.
    ENVIRONMENT = property(lambda self: self.__class__.__name__)
    # MAIL_EXCEPTION_THROTTLE = 24 * 60 * 60
    _SQLALCHEMY_TRACK_MODIFICATIONS = False
    _SQLALCHEMY_DATABASE_DATABASE = 'jvercout_flaskr'
    _SQLALCHEMY_DATABASE_HOSTNAME = 'localhost'
    _SQLALCHEMY_DATABASE_USERNAME = 'jerome'
    _SQLALCHEMY_DATABASE_PASSWORD = 'placebo'


class CeleryConfig(HardCoded):
    """Configurations used by Celery only."""
    # CELERYD_PREFETCH_MULTIPLIER = 1
    # CELERYD_TASK_SOFT_TIME_LIMIT = 20 * 60  # Raise exception if task takes too long.
    # CELERYD_TASK_TIME_LIMIT = 30 * 60  # Kill worker if task takes way too long.
    # CELERY_ACCEPT_CONTENT = ['json']
    # CELERY_ACKS_LATE = True
    # CELERY_DISABLE_RATE_LIMITS = True
    # CELERY_IMPORTS = ('pypi',)
    # CELERY_RESULT_SERIALIZER = 'json'
    # CELERY_TASK_RESULT_EXPIRES = 10 * 60  # Dispose of Celery Beat results after 10 minutes.
    # CELERY_TASK_SERIALIZER = 'json'
    # CELERY_TRACK_STARTED = True
    CELERY_RESULT_BACKEND = 'redis://localhost/'
    CELERY_BROKER_URL = 'redis://localhost/1'
    # CELERYBEAT_SCHEDULE = {
    #     'pypy-every-day': dict(task='pypi.update_package_list', schedule=crontab(hour='0')),
    # }


class Config(CeleryConfig):
    """Default Flask configuration inherited by all environments. Use this for development environments."""
    DEBUG = True
    TESTING = False
    # SECRET_KEY = "i_don't_want_my_cookies_expiring_while_developing"
    # MAIL_SERVER = 'smtp.localhost.test'
    # MAIL_DEFAULT_SENDER = 'admin@demo.test'
    # MAIL_SUPPRESS_SEND = True
    # REDIS_URL = 'redis://localhost/0'
    # SQLALCHEMY_DATABASE_URI = property(lambda self: 'postgresql://{u}:{p}@{h}/{d}'.format(
    #     d=urlparse(self._SQLALCHEMY_DATABASE_DATABASE), h=urlparse(self._SQLALCHEMY_DATABASE_HOSTNAME),
    #     p=urlparse(self._SQLALCHEMY_DATABASE_PASSWORD), u=urlparse(self._SQLALCHEMY_DATABASE_USERNAME)
    # ))
    SQLALCHEMY_DATABASE_URI='postgresql://jerome:toto@localhost/jvercout_flaskr'

class Testing(Config):
    TESTING = True
    # CELERY_ALWAYS_EAGER = True
    # REDIS_URL = 'redis://localhost/1'
    # _SQLALCHEMY_DATABASE_DATABASE = 'lsp_1'
    # _SQLALCHEMY_DATABASE_PASSWORD = 'passwordlsp'
    # _SQLALCHEMY_DATABASE_USERNAME = 'lsp'


class Production(Config):
    DEBUG = False
    # SECRET_KEY = None
    # ADMINS = ['my-team@me.test']
    # MAIL_SUPPRESS_SEND = False
    # STATICS_MINIFY = True
