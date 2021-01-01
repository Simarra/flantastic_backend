from flantastic_backend.flantastic_backend.app import create_app, db
from flantastic_backend.flantastic_backend.models import User, Bakery, Role

app = create_app()
db.create_all()

app.app_context().push()

a_role = Role(role_name="Administrateur")

mybak = Bakery(name="coucou", comment="salut", rate=1) 
an_user =  User(username='loic', password='lol', email="coucou")
an_user.role.append(a_role)

an_user.bakery.append(mybak)

db.session.add(an_user)
db.session.commit()