import json

import spacy
from fastapi import HTTPException
from sqlalchemy.orm import Session

from demandes.model import DemandesInfo
from register_login.model import User
from utils.email import send_email

nlp = spacy.load("en_core_web_sm")


def submit_request(text: str, db: Session, user_id: int):
    payload = {
        "text": text,
        "user_id": user_id
    }
    info_demand = DemandesInfo(**payload)
    db.add(info_demand)
    db.commit()
    db.refresh(info_demand)
    return info_demand


def get_requests(db: Session, user_id: int):
    result = db.query(DemandesInfo).filter(DemandesInfo.user_id == user_id).all()
    return result


def update_request(db: Session, request_id: int, status: str):
    request_to_update = db.query(DemandesInfo).filter(DemandesInfo.id == request_id).first()

    if not request_to_update:
        raise HTTPException(status_code=404, detail="Request not found")

    user_id = request_to_update.user_id
    user = db.query(User).filter(User.id == user_id).first()
    user_email = user.email
    send_email(user_email, f"Votre demande de pret a été {status}", "Visiter notre page pour voir plus de detail")

    request_to_update.status = status
    db.commit()
    db.refresh(request_to_update)
    return request_to_update

