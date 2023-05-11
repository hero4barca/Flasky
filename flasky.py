import os, sys, click, subprocess
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, app=app)

@app.cli.command()
@click.option('--coverage/--no-coverage', default=False, 
              help='Run tests under code coverage.') # starts coverage
@click.option("--testname", default=None, 
              help = 'Retrieves test modules, classes or methods by given name' ) # specifies tests to run
def test(coverage, testname):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        os.environ['FLASK_COVERAGE'] = '1'
        # os.execvp(sys.executable, [sys.executable] + sys.argv)
        subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])

    import unittest
    if testname :
        discovered_tests = unittest.TestLoader().loadTestsFromName(testname)
    else:
        discovered_tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(discovered_tests)

    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()

