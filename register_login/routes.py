from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from starlette import status

from register_login.controller import login_user, create_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from register_login.model import User
from register_login.schemas import LoginSchema, RegisterSchema
from sqlalchemy.orm import Session

from dependencies import get_db, create_jwt_token

auth_routes = APIRouter()


@auth_routes.post('/login')
def login(login: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login.email).first()
    if not user or not user.verify_password(login.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_jwt_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_routes.post("/register")
def register(user_data: RegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = create_user(db, user_data)
    return {"message": "User successfully registered"}