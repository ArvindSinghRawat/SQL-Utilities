import os
import unittest
import coverage

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db

# Models
from app.main.model import user

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def run_coverage():
    """Runs the unit tests with Coverage Report"""
    cov = coverage.Coverage()
    cov.start()

    val = 1

    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=0).run(tests)
    if result.wasSuccessful():
        val = 0

    cov.stop()
    cov.save()

    cov.html_report()
    cov.report()
    return val


if __name__ == '__main__':
    manager.run()
