import json

import spacy
from sqlalchemy.orm import Session

from demandes.model import DemandesInfo
from ia.extract import ExtractIa


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

    if request_to_update:
        request_to_update.status = status
        db.commit()
        db.refresh(request_to_update)
        return request_to_update
    else:
        return None
