from pydantic import BaseModel

class LoginSchema(BaseModel):
    email: str
    password: str

class RegisterSchema(BaseModel):
    nom: str
    prenom: str
    adresse: str
    num_tel: str
    email: str
    password: str