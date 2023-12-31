from fastapi import APIRouter

extract_routes = APIRouter()

@extract_routes.post('/extract')
def extraction():
  return {"message": "User successfully extracted"}