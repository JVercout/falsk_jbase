import signal
import sys

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app.application import create_app, get_config
from app.extensions import db

# Migrations commands
app = create_app(get_config('app.config.Config'))
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda *_: sys.exit(0))  # Properly handle Control+C
    manager.run()
