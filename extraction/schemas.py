from pydantic import BaseModel

class TextSchema(BaseModel):
    text: str
    request_id: str
