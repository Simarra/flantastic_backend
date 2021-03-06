from flantastic_backend.flantastic_backend.models import db
from sqlalchemy.orm import relationship
import datetime


class Vote(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    gout = db.Column(db.SmallInteger, nullable=False)
    pate = db.Column(db.SmallInteger, nullable=False)
    texture = db.Column(db.SmallInteger, nullable=False)
    apparence = db.Column(db.SmallInteger, nullable=False)
    commentaire = db.Column(db.String(250), nullable=True)
    date_updated = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=True,
    )
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    user = relationship("User", back_populates="vote")

    bakery_id = db.Column(db.Integer, db.ForeignKey("bakery.id"), primary_key=True)
    bakery = relationship("Bakery", back_populates="vote")

    @db.validates("gout")
    @db.validates("pate")
    @db.validates("texture")
    @db.validates("apparence")
    def validate_five_start(self, key: str, value: int):
        assert (value <= 5) and (value >= 0)
        return value

    # def __repr__(self):
    #     return '<Vote %r>' % self.id