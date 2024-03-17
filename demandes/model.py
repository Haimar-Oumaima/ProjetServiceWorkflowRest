from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class DemandesInfo(Base):
    __tablename__ = "demandes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(255))
    user_id = Column(Integer)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    status = Column(Enum("pending", "approved", "refused", name="request_status_enum"), default="pending")

