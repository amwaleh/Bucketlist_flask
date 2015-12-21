from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os
import sys

sys.path.append('.')
from app.bucketlist import app, db
app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()