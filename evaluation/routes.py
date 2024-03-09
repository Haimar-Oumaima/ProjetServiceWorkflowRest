from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import model, schemas, controller
from dependencies import get_db

evaluation_router = APIRouter()

@evaluation_router.post("/evaluate")
def extract_text(text_schema: schemas.TextSchema, db: Session = Depends(get_db)):
    try:
        result = controller.evaluate_property_value(db=db, description=text_schema.description, request_id=text_schema.request_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))