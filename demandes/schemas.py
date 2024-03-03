from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class RequestSchema(BaseModel):
    text: str
