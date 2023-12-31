from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))  # Ajoutez une longueur ici
    last_name = Column(String(100))  # Et ici
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(128))  # Et ici
    phone_number = Column(String(15))  # Et ici
    postal_address = Column(String(200))  # Et ici
    is_active = Column(Boolean, default=True)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
