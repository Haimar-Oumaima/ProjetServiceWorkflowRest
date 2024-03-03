from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db, get_token_from_header, get_user_from_token
from . import controller, schemas, model


requests_routes = APIRouter()
@requests_routes.post("/submit")
def extract_text(schema: schemas.RequestSchema, db: Session = Depends(get_db),token: str = Depends(get_token_from_header)):
    user_payload = int(get_user_from_token(token))
    try:
        created_request = controller.submit_request(text=schema.text, db=db, user_id=user_payload)
        return created_request
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
