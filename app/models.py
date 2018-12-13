from datetime import datetime
from app import db

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    searchword = db.Column(db.String(60), unique=True)
    count = db.Column(db.Integer)
    dateSearched = db.Column(db.DateTime, default = datetime.utcnow)

def __repr__(self):
    return '<Searched for {}>'.format(self.searchword)
