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