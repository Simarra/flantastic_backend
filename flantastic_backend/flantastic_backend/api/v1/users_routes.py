from flask import Blueprint, jsonify, request
from flantastic_backend.flantastic_backend.models.users import users


# Blueprint Configuration
flantastic_users_bp = Blueprint(
    'flantastic', __name__, url_prefix='/v1/users'
)

@flantastic_users_bp.route('/users', methods=["GET"])
@flantastic_users_bp.route('/', methods=["GET"])
def get_users():
    return jsonify(users)

@flantastic_users_bp.route('/user/<username>', methods=["GET"])
def get_user(username: str):
    return jsonify(users)
    
@flantastic_users_bp.route('/adduser', methods=["POST"])
def add_user():
    content = request.json
    if len(content["username"]) > 0:
        users.append(request.json)
    return  "OK", 200

@flantastic_users_bp.route('/deluser', methods=["POST"])
def add_user():
    return  "OK", 200