import requests
from fastapi import FastAPI
from sqlalchemy import event

import database
from demandes.model import DemandesInfo
from extraction.model import ExtractedInfo
from register_login.model import User
from register_login.routes import auth_routes
from extraction.routes import extract_routes
from demandes.routes import requests_routes
from scoring.routes import scoring_routes

User.metadata.create_all(bind=database.engine)
ExtractedInfo.metadata.create_all(bind=database.engine)
DemandesInfo.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_routes, prefix="/login_register", tags=["Register & Login"])

app.include_router(requests_routes, prefix="/requests", tags=["Extraction d'Informations (IE)"])

app.include_router(extract_routes, prefix="/extraction", tags=["Extraction d'Informations (IE)"])

app.include_router(scoring_routes, prefix="/scoring", tags=["Scoring & credit verification"])

# app.include_router(evaluation_router, prefix="/evaluation_propriete", tags=["Évaluation de la Propriété"])


def service_web_composite(mapper, connection, target):
    request_id = str(target.id)
    text = target.text
    url_to_extract_data = "http://127.0.0.1:8000/extraction/extract"
    payload_to_extract_data = {"request_id": request_id, "text": text}
    response_extract = requests.post(url_to_extract_data, json=payload_to_extract_data)
    print(response_extract.status_code)
    if response_extract.status_code != 200:
        # normalement error
        return
    # continuer avec les autres services, appeler le scoring, le propriete et decision




event.listen(DemandesInfo, 'after_insert', service_web_composite)