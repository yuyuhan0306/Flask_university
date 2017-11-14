import os
# from flask.ext.script import Manager
# from flask.ext.migrate import Migrate, MigrateCommand

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

# set the config to get our environment
app.config.from_object(os.environ['APP_SETTINGS'])


# creat a migrate instance, with app and db as the arguments
migrate = Migrate(app, db)
# set up a manager command to initialize a Manager instance for our app
manager = Manager(app)


# add the db command to the manager so that we can run the migrations from the command line
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()