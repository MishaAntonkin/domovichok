from datetime import datetime

from . import db


class BaseDBModel(db.Model):
    __abstract__ = True

    def row2dict(row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = getattr(row, column.name)

        return d

    def update(self, new_data):
        for key in new_data.keys():
            if key not in self.__table__.columns:
                continue
            elif key == 'id':
                continue
            if getattr(self, key) != new_data.get(key):
                setattr(self, key, new_data.get(key))


class Flat(BaseDBModel):
    id = db.Column(db.Integer, primary_key=True, index=True)
    district = db.Column(db.String(20), index=True)
    name = db.Column(db.String(100), index=True)
    price = db.Column(db.Float(precision=2))
    area = db.Column(db.Float(precision=2), index=True)
    currency = db.Column(db.String(3), index=True)
    url = db.Column(db.Text(), index=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.id)
