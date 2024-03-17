from pydantic import BaseModel

class ScoringResponse(BaseModel):
    eligibility_result: str
    score: int
    max_possible_score: int

class PropertyEvaluationResponse(BaseModel):
    request_id: int
    market_value: float
    legal_compliance: str
    inspection_report: str
