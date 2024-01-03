# extraction_info/schemas.py
from pydantic import BaseModel
from typing import List, Optional

class LoanApplicationSchema(BaseModel):
    text: str

class ExtractedInfoSchema(BaseModel):
    name: Optional[str]
    address: Optional[str]
    money: Optional[str]
    # Autres champs selon vos besoins

class ExtractionResponseSchema(BaseModel):
    extracted_infos: List[ExtractedInfoSchema]
