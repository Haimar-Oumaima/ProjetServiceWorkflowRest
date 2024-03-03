from fastapi import FastAPI
import database
from register_login.model import User
from register_login.routes import auth_routes
from extraction.routes import extract_routes

User.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_routes, prefix="/login_register", tags=["Register & Login"])

app.include_router(extract_routes, prefix="/extraction", tags=["Extraction d'Informations (IE)"])

app.include_router(evaluation_router, prefix="/evaluation_propriete", tags=["Évaluation de la Propriété"])

