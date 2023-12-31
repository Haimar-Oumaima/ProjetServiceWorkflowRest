from fastapi import APIRouter, Depends, HTTPException, status
from starlette import status

from auth.controller import login_user, create_user
from auth.model import User
from auth.schemas import LoginSchema, RegisterSchema
from sqlalchemy.orm import Session

from dependencies import get_db

auth_routes = APIRouter()


@auth_routes.post('/login')
def login(login_data: LoginSchema, db: Session = Depends(get_db)):
    user = login_user(login_data, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    return {"message": "User successfully logged in"}


@auth_routes.post("/register")
def register(user_data: RegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = create_user(db, user_data)
    return {"message": "User successfully registered"}