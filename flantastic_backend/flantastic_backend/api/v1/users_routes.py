from flask import Blueprint, jsonify, request
from flantastic_backend.flantastic_backend.models import User, db
from flantastic_backend.flantastic_backend.api.auth.basic_auth import auth


# Blueprint Configuration
flantastic_users_bp = Blueprint("flantastic_users", __name__, url_prefix="/api/v1/users")


@flantastic_users_bp.route("/", methods=["GET"])
@auth.login_required
def get_users():
    """
    Optinal param: limit to limit number of users fetch
    """
    nb_of_users = request.args.get('limit')

    
    if not nb_of_users:
        nb_of_users = 10
    nb_of_users = int(nb_of_users)

    users_res = User.query.limit(nb_of_users).all()
    res_list = []
    for user in users_res:
        dct = {"username": user.username}
        res_list.append(dct)

    return jsonify(res_list)


@flantastic_users_bp.route("/", methods=["POST"])
def add_user():
    content = request.json

    have_username = content["username"]
    have_pwd = content["password"]
    have_mail = content["email"]

    if not (have_username and have_pwd and have_mail):
        return "Username and paswword must be provided", 404

    if len(content["username"]) < 3:
        return "Username must be at least 3", 404
    if len(content["password"]) < 3:
        return "Password must be at least 3", 404
    if len(content["email"]) < 3:
        return "email must be at least 3", 404

    username_exists = User.query.filter(
        User.username == content["username"]
    ).one_or_none()
    if username_exists is not None:
        return "Username {} already exists".format(content["username"]), 404

    new_user = User(
        username=content["username"],
        password=content["password"],
        email=content["email"],
    )
    db.session.add(new_user)
    db.session.commit()

    return "ok", 200



# @flantastic_users_bp.route('/deluser', methods=["POST"])
# def del_user():
#     return  "OK", 200
# @flantastic_users_bp.route('/user/<username>', methods=["GET"])
# def get_user(username: str):
#     return jsonify(users)