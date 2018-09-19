from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	db.init_app(app)
	login_manager.init_app(app)
	login_manager.login_message = "You must be logged in"
	login_manager.login_view = 'auth.login'
	migrate = Migrate(app, db)
	Bootstrap(app)

	from app import models

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix ='/api')

	from .users import users as users_blueprint
	app.register_blueprint(users_blueprint)

	return app