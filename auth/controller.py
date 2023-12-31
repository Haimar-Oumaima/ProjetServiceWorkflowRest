from passlib.context import CryptContext
from sqlalchemy.orm import Session

from auth.model import User
from auth.schemas import LoginSchema, RegisterSchema


def login_user(login: LoginSchema, db: Session):
    user = db.query(User).filter(User.email == login.email).first()
    if not user or not user.verify_password(login.password):
        return None
    return user

def create_user(db: Session, user: RegisterSchema):
    db_user = User(email=user.email)
    db_user.hash_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user