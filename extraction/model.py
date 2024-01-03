# extraction_info/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class ExtractedInfo(Base):
    __tablename__ = "extracted_infos"
    id = Column(Integer, primary_key=True, index=True)
    loan_application_id = Column(Integer, ForeignKey("loan_applications.id"))
    name = Column(String)
    address = Column(String)
    money = Column(String)
    # Autres champs selon vos besoins

class LoanApplication(Base):
    __tablename__ = "loan_applications"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    extracted_infos = relationship("ExtractedInfo", back_populates="loan_application")
