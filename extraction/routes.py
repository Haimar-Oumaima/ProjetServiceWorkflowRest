from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db

import database
from extraction import controller, schemas

extract_routes = APIRouter()

@extract_routes.post('/extract')
def extract_and_store_info(request: schemas.LoanApplicationSchema, db: Session = Depends(get_db)):
  extracted_info = controller.extract_information(request.text)
  stored_data = controller.extract_information(db, extracted_info)
  return {"message": "Data stored successfully", "data": stored_data}