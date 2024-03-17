from passlib.context import CryptContext
from sqlalchemy.orm import Session
import random
from register_login.model import User
from register_login.schemas import LoginSchema, RegisterSchema



from datetime import datetime, timedelta
from jose import jwt



# Configuration de JWT
SECRET_KEY = "votre_clé_secrète_ici"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # La durée de vie du token


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def login_user(login: LoginSchema, db: Session):
    user = db.query(User).filter(User.email == login.email).first()
    if not user or not user.verify_password(login.password):
        return None
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def create_user(db: Session, user: RegisterSchema):
    db_user = User(
        email=user.email,
        nom=user.nom,
        prenom=user.prenom,
        adresse=user.adresse,
        num_tel=user.num_tel
    )
    db_user.hash_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    user_id = db_user.id 

    add_user_history_entry(db, user_id)  # Add the history of the newly created user.
    
    return db_user

def add_user_history_entry(db: Session, user_id: int):
    from .model import UserHistory

    debts = random.randint(0, 5)
    late_payments = random.randint(0, 10)
    bankruptcy = random.choice([0, 1])
    monthly_revenue = random.uniform(2000, 6000)
    monthly_expenses = random.uniform(500, monthly_revenue - 100)

    user_history_entry = UserHistory(
        user_id=user_id,
        debts=debts,
        late_payments=late_payments,
        bankruptcy=bankruptcy,
        monthly_revenue=monthly_revenue,
        monthly_expenses=monthly_expenses
    )

    db.add(user_history_entry)
    db.commit()
    db.refresh(user_history_entry)
    
def get_user_id(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return user.id
    return None