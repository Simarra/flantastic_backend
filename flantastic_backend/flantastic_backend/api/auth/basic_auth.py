from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flantastic_backend.flantastic_backend.models import User, Role
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user_found = User.query.filter(User.username == username).first()

    if user_found:
       if user_found.password == password:
           return username
    # if username in User.query.all() and \
    #         check_password_hash(users.get(username), password):