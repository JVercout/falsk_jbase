from app.extensions import db
from app.models.history_meta import Versioned


class Watch(Versioned, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<Watch %r>' % self.id
