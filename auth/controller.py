from passlib.context import CryptContext
from sqlalchemy.orm import Session
import random
from auth.model import User
from auth.schemas import LoginSchema, RegisterSchema


def login_user(login: LoginSchema, db: Session):
    user = db.query(User).filter(User.email == login.email).first()
    if not user or not user.verify_password(login.password):
        return None
    return user

def create_user(db: Session, user: RegisterSchema):
    db_user = User(
        email = user.email,
        nom = user.nom,
        prenom = user.prenom,
        adresse = user.adresse,
        num_tel = user.num_tel
    )
    db_user.hash_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    add_user_history_entry(db, user.email)
    
    return db_user

def add_user_history_entry(db: Session, email: str):
    from auth.model import UserHistory

    debts = random.randint(0, 5)
    late_payments = random.randint(0, 10)
    bankruptcy = random.choice([0, 1])

    user_history_entry = UserHistory(email=email, debts=debts, late_payments=late_payments, bankruptcy=bankruptcy)

    db.add(user_history_entry)
    db.commit()
    db.refresh(user_history_entry)