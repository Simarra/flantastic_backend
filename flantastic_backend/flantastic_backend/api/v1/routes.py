from flask import Blueprint


# Blueprint Configuration
flantastic_bp = Blueprint(
    'flantastic', __name__, url_prefix='/v1'
)

@flantastic_bp.route('/')
def hello_world():
    return 'Hello, World!'

