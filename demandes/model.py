from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Enum, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class DemandesInfo(Base):
    __tablename__ = "demandes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255))
    user_id = Column(Integer)
    status = Column(Enum("pending", "approved", "rejected", name="request_status_enum"), default="pending")







