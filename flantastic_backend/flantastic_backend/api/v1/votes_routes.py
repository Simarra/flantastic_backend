from flask import Blueprint, jsonify, request
from flantastic_backend.flantastic_backend.models import User, Vote, db
from flantastic_backend.flantastic_backend.api.auth.basic_auth import auth


# Blueprint Configuration
flantastic_votes_bp = Blueprint("flantastic_votes", __name__, url_prefix="/api/v1/")


@flantastic_votes_bp.route("/votes", methods=["GET"])
@auth.login_required
def get_user_votes():
    """
    User must be logged.
    Optinal param: limit to limit number of votes fetch
    """
    nb_of_votes = request.args.get("limit")
    user = auth.current_user()

    if not nb_of_votes:
        nb_of_votes = 10
    nb_of_votes = int(nb_of_votes)

    users_votes = Vote.query.filter(User.username == user).limit(nb_of_votes).all()
    res_list = []
    for vote in users_votes:
        dct = {
            "gout": vote.gout,
            "pate": vote.pate,
            "texture": vote.texture,
            "apparence": vote.apparence,
            "commentaire": vote.commentaire,
            "date_updated": vote.date_updated,
            "date_created": vote.date_created,
            "bakery_name": vote.bakery.name,
            "bakery_id": vote.bakery.id,
        }
        res_list.append(dct)

    return jsonify(res_list)