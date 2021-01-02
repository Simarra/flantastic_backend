from flantastic_backend.flantastic_backend.models import db
from sqlalchemy.orm import relationship

class Bakery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(120), unique=True, nullable=False)

    vote = relationship("Vote", back_populates="bakery")
    def __repr__(self):
        return '<User %r>' % self.name