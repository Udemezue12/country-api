from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_cors import CORS










from country_project.database_config import application

db = SQLAlchemy(application)
migrate = Migrate(application, db)

mail = Mail(application)
bcrypt = Bcrypt(application)
csrf = CSRFProtect(application)
login_manager = LoginManager(application)
