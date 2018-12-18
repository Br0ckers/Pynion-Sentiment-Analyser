from datetime import datetime
from app import db, Base

class Pynionquery(Base):
    __tablename__ = 'Pynionquery'
    id = db.Column(db.Integer, primary_key=True)
    searchword = db.Column(db.String(60), unique=True)
    count = db.Column(db.Integer)
    dateSearched = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"Query('{self.searchword}', {self.count} , {self.id})"

    def __init__(self, searchword):
        self.searchword = searchword
        self.count = 1
