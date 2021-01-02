from flantastic_backend.flantastic_backend.models import db
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
    nullable=False)

    role = relationship("Role", back_populates="user")
    vote = relationship("Vote", back_populates="user")


    def __repr__(self):
        return '<User %r>' % self.username