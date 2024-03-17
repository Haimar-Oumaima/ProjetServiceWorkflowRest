from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Decision(Base):
    __tablename__ = 'decisions'
    id = Column(Integer, primary_key=True)
    request_id = Column(Integer)
    decision = Column(String(255))
    message = Column(String(255))
    reason = Column(String(255))
    interest_rate = Column(String(255))
    monthly_amount = Column(String(255))
