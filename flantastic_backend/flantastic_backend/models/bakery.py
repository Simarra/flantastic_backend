bakeries_rates = {
    "id": 1,
    "userfrom": "Loïc",
    "rate": 1,
    "Comment": "no comment guy"
}

from flantastic_backend.flantastic_backend.models import db

class Bakery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    comment = db.Column(db.String(120), unique=True, nullable=False)
    rate = db.Column(db.Integer, primary_key=True)

    user_from_id = db.Column(db.Integer, db.ForeignKey('user.id'),
    nullable=False)
    user = db.relationship('User',
        backref=db.backref('user', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username