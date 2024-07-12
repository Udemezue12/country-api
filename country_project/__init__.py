from clean import app
from country_project.core.views import core
from country_project.error_pages.handlers import error_pages
from country_project.login import login_manager
from country_project.users.views import users
from country_project.passenger.views import passenger
# from country_project.driver.views import driver
from country_project.code.states import state
from country_project.country.country_list import country, my_state
from country_project.database import db, mail, application
from country_project.secure import secure
from config import Config

app.register_blueprint(core)
# app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(state)

app.register_blueprint(secure)
app.register_blueprint(passenger, url_prefix='/passenger')
app.register_blueprint(my_state)
app.register_blueprint(country)

login_manager.init_app(app)
mail.init_app(app)

# db.init_app(app)
app.config.from_object(Config)

app.template_folder = 'country_project/templates/'
app.static_folder = 'country_project/static'
