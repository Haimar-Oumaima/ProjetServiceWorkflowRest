from decision.controller import make_decision
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from decision.schemas import ScoringResponse, PropertyEvaluationResponse
from dependencies import get_db

decision_routes = APIRouter()

@decision_routes.post("/decide")
def make_decision_route(scoring_response: ScoringResponse, property_evaluation_response: PropertyEvaluationResponse, db: Session = Depends(get_db)):
    decision = make_decision(db, scoring_response, property_evaluation_response)
    return decision
