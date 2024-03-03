from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ExtractedInfo(Base):
    __tablename__ = "extrac_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom_client = Column(String(255))
    description_propriete = Column(String(255))
    adresse_propriete = Column(String(255))
    montant_pret = Column(String(255))
    duree_pret = Column(String(255))
    revenu_mensuel = Column(String(255))
    depenses_mensuelles = Column(String(255))
    request_id = Column(Integer)



