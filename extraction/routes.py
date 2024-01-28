from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from . import controller, schemas, model

extract_routes = APIRouter()

@extract_routes.post("/extract")
def extract_text(text_schema: schemas.TextSchema, db: Session = Depends(get_db)):
    try:
        result = controller.extract_information(text_schema.text, db)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
