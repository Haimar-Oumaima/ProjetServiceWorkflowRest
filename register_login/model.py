from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
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
    history_entries = relationship("UserHistory", back_populates="user")

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)

    def hash_password(self, plain_password):
        self.hashed_password = pwd_context.hash(plain_password)
    
class UserHistory(Base):
    __tablename__ = "user_history"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="history_entries") 
    debts = Column(Integer) 
    late_payments = Column(Integer)
    bankruptcy = Column(Integer)
    monthly_revenue = Column(Float)
    monthly_expenses = Column(Float)
