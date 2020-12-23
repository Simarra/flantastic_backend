from flask import Flask
from flantastic_backend.flantastic_backend.api.v1.routes import flantastic_bp

flantastic_app = Flask(__name__)
flantastic_app.register_blueprint(flantastic_bp)