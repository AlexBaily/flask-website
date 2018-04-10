from . import db


class Development(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    details = db.Column(db.String(80))
    properties = db.relationship('Property', backref='development',
                                 lazy=True)

    def __repr__(self):
        return '<Development %r' % self.name

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    development_id = db.Column(db.Integer, db.ForeignKey('development.id'))

    def __repr__(self):
        return '<Property %r' % self.name

