from pydantic import BaseModel

class ScoreSchema(BaseModel):
    user_id: int


class ScoreResponse(BaseModel):
    eligibility_result: str
    score: int
    max_possible_score: int
