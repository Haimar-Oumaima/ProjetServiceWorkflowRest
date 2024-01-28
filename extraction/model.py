from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ExtractedInfo(Base):
    __tablename__ = "extrac_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom_client = Column(String)
    description_propriete = Column(String)
    adresse_propriete = Column(String)
    montant_pret = Column(String)  # Utilisez Integer pour les montants si ce sont des nombres
    duree_pret = Column(String)  # Utilisez Integer pour la durée si c'est un nombre d'années
    revenu_mensuel = Column(String)  # Assurez-vous que c'est le type approprié
    depenses_mensuelles = Column(String)  # Assurez-vous que c'est le type approprié



