from flask import Flask
from flantastic_backend.flantastic_backend.api.v1.users_routes import flantastic_users_bp

flantastic_app = Flask(__name__)
flantastic_app.register_blueprint(flantastic_users_bp, url_prefix="")
flantastic_app.register_blueprint(flantastic_users_bp)