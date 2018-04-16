from . import db


class BaseDBModel(db.Model):
    __abstract__ = True

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))

        return d


class Flat(BaseDBModel):
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(20), index=True)
    name = db.Column(db.String(100), index=True)
    price = db.Column(db.Float(precision=2))

    def __repr__(self):
        return '<User {}>'.format(self.id)
