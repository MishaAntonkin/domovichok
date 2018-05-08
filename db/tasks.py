from datetime import datetime, timedelta


from app.models import *
from app import db


CLEAN_TIME = timedelta(days=7)


def clean_old_flats():
    time_7da = datetime.now() - CLEAN_TIME
    old_flats = Flat.query.filter(Flat.date_updated <= time_7da).all()
    for fl in old_flats:
        #db.session.delete(fl)
    #db.session.commit()

clean_old_flats()