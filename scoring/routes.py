from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .controller import calculate_score
from .schemas import ScoreSchema
from .schemas import ScoreResponse
from dependencies import get_db

scoring_routes = APIRouter()

@scoring_routes.post("/scoring", response_model=ScoreResponse)
def calculate_score_route(score_request: ScoreSchema, db: Session = Depends(get_db)):
    user_id = score_request.user_id
    try:
        score = calculate_score(db, user_id)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))
    max_possible_score = 10
    eligibility_result = (
        f"User is not eligible with a score of {score}/{max_possible_score}"
        if score < 5
        else f"User is eligible with a score of {score}/{max_possible_score}"
    )

    return {"score": score, "max_possible_score": max_possible_score, "eligibility_result": eligibility_result}