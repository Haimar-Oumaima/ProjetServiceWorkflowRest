from decision.controller import make_decision, get_decision
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from decision.schemas import ScoringResponse, PropertyEvaluationResponse
from dependencies import get_db

decision_routes = APIRouter()

@decision_routes.post("/decide")
def make_decision_route(scoring_response: ScoringResponse, property_evaluation_response: PropertyEvaluationResponse, db: Session = Depends(get_db)):
    decision = make_decision(db, scoring_response, property_evaluation_response)
    return decision


@decision_routes.get("/request/{request_id}")
def update_request(request_id: int, db: Session = Depends(get_db)):
    try:
        return get_decision(db=db, request_id=request_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))