from datetime import datetime
from app import  Base
from sqlalchemy import Column, Integer, String, DateTime

class Pynionquery(Base):
    __tablename__ = 'Pynionquery'
    id = Column(Integer, primary_key=True)
    searchword = Column(String(60), unique=True)
    count = Column(Integer)
    dateSearched = Column(DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"Query('{self.searchword}', {self.count} , {self.id})"

    def __init__(self, searchword):
        self.searchword = searchword
        self.count = 1
