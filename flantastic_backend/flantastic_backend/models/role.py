from flantastic_backend.flantastic_backend.models import db
from sqlalchemy.orm import relationship

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)

    user = relationship("User", back_populates="role")

    def __repr__(self):
        return '<roleName %r>' % self.role_name
