import os
from datetime import timedelta
from country_project import app

application = app
basedir = os.path.abspath(os.path.dirname(__file__))

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'country.db')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['USE_SESSION_FOR_NEXT'] = True
application.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=20)

if __name__ == '__main__':
    app.run()
