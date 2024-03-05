from pydantic import BaseModel

class TextSchema(BaseModel):
    description: str
    request_id: str

