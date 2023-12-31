from fastapi import FastAPI
import database
from auth.model import User
from auth.routes import auth_routes
from extraction.routes import extract_routes

User.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_routes, prefix="/auth")
app.include_router(extract_routes, prefix="/extraction")
