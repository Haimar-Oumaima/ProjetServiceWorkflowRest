from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nom = Column(String(255))  # Ajout du champ nom
    prenom = Column(String(255))  # Ajout du champ prenom
    adresse = Column(String(255))  # Ajout du champ adresse
    num_tel = Column(String(20))  # Ajout du champ numéro de téléphone
    email = Column(String(255), unique=True)
    hashed_password = Column(String(255))

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)

    def hash_password(self, plain_password):
        self.hashed_password = pwd_context.hash(plain_password)
