from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os
import sys

sys.path.append('.')
from api.bucketlist import app, db


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()