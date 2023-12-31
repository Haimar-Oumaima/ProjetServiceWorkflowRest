from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    postal_address: str
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    postal_address: str
    is_active: bool

    class Config:
        from_attributes = True