from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

login_manager.login_view = 'user_routes.page_login'
login_manager.login_message = 'Por favor, realize o login'
login_manager.login_message_category = 'info'

from web.routes.user_route import user_blueprint
from web.routes.home_route import home_blueprint
from web.routes.category_route import category_blueprint
from web.routes.product_route import product_blueprint
from web.routes.errors_route import errors_blueprint

from web.models import user_model, category_model, product_model

app.register_blueprint(user_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(errors_blueprint)
