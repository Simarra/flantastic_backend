from flantastic_backend.flantastic_backend.app import create_app, db
from flantastic_backend.flantastic_backend.models import User, Bakery, Role, Vote

app = create_app()
app.app_context().push()
db.create_all()


admin_role = Role(role_name="Administrateur")
user_role = Role(role_name="Utilisateur")

mybak = Bakery(name="coucou", comment="salut") 
an_user =  User(username='loic', password='lol', email="coucou")
an_user.role = admin_role

a_vote = Vote(gout=5, pate=3, texture=1, apparence=2, user=an_user, bakery=mybak)

db.session.add(a_vote)
db.session.add(user_role)
db.session.commit()