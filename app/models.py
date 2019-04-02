from datetime import datetime
import time
from app import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    altitude = db.Column(db.Numeric(10,10))
    longitude = db.Column(db.Numeric(10,10))
    latitude = db.Column(db.Numeric(10,10))
    airspeed = db.Column(db.Integer)
    time = db.Column(db.String(120))
    def __repr__(self):
        return '<Data {}>'.format(self.time)

