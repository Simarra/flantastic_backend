from flask import Flask
from flantastic_backend.flantastic_backend.api.v1.users_routes import flantastic_users_bp
from flantastic_backend.flantastic_backend.api.v1.votes_routes import flantastic_votes_bp
from flantastic_backend.flantastic_backend.models import db
from flantastic_backend.flantastic_backend.config import DevelopmentConfig



def create_app():
    flantastic_app = Flask(__name__)
    flantastic_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp.db'
    db.init_app(flantastic_app)

    # flantastic_app.register_blueprint(flantastic_users_bp, url_prefix="")
    flantastic_app.register_blueprint(flantastic_users_bp)
    flantastic_app.register_blueprint(flantastic_votes_bp)
    flantastic_app.config.from_object(DevelopmentConfig())

    return flantastic_app