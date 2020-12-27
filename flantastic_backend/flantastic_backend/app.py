from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flantastic_backend.flantastic_backend.api.v1.users_routes import flantastic_users_bp
from flantastic_backend.flantastic_backend.models import db

flantastic_app = Flask(__name__)

flantastic_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db.init_app(flantastic_app)


flantastic_app.register_blueprint(flantastic_users_bp, url_prefix="")
flantastic_app.register_blueprint(flantastic_users_bp)