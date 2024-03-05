from sqlalchemy import Column, Integer, String, Float
from database import Base

class PropertyEvaluation(Base):
    __tablename__ = 'property_evaluations'
    id = Column(Integer, primary_key=True, index=True)

    request_id = Column(Integer)
    market_value = Column(Float)
    inspection_report = Column(String(255))
    legal_compliance = Column(String(255))
