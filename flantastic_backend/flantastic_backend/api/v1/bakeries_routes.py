
from flask import Blueprint, jsonify, request
from flantastic_backend.flantastic_backend.models import User, Bakery


# Blueprint Configuration
flantastic_users_bp = Blueprint("flantastic", __name__, url_prefix="/api/v1/bakeries")


@flantastic_users_bp.route("/", methods=["GET"])
def get_bakeries():
    """
    url param limit : to limit number of bakeries to fetch
    url param user :  to get all bakeries related to user.
    
    body param ids : view OSM elts.
    """
    limit_nb = request.args.get('limit')
    user_filter = request.args.get('user')

    body = request.content
    params_ids = body.get("params_ids")

    return "OK", 200

@flantastic_users_bp.route("/", methods=["POST", "PUT"])
def add_or_update_bakeriy():
    """
    body param id : OSM id.
    body param: user_from: user wich rate
    """

    body = request.content
    item_id = body.get("params_ids")

    return "OK", 200