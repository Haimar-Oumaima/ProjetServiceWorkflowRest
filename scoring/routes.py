from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .controller import calculate_score, get_user_history
from .schemas import ScoreSchema
from .schemas import ScoreResponse
from dependencies import get_db

scoring_routes = APIRouter()

@scoring_routes.post("/scoring", response_model=ScoreResponse)
def calculate_score_route(score_request: ScoreSchema, db: Session = Depends(get_db)):
    user_id = score_request.user_id
    score = calculate_score(db, user_id)
    max_possible_score = 10

    eligibility_result = (
        f"User is not eligible with a score of {score}/{max_possible_score}"
        if score < 5
        else f"User is eligible with a score of {score}/{max_possible_score}"
    )

    return {"score": score, "max_possible_score": max_possible_score, "eligibility_result": eligibility_result}