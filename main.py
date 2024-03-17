import json

import requests
from fastapi import FastAPI
from sqlalchemy import event

import database
from demandes.model import DemandesInfo
from evaluation.model import PropertyEvaluation
from evaluation.routes import evaluation_router
from extraction.model import ExtractedInfo
from register_login.model import User
from register_login.routes import auth_routes
from extraction.routes import extract_routes
from demandes.routes import requests_routes
from scoring.routes import scoring_routes
from decision.routes import decision_routes

User.metadata.create_all(bind=database.engine)
ExtractedInfo.metadata.create_all(bind=database.engine)
DemandesInfo.metadata.create_all(bind=database.engine)
PropertyEvaluation.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(auth_routes, prefix="/login_register", tags=["Register & Login"])

app.include_router(requests_routes, prefix="/requests", tags=["Extraction d'Informations (IE)"])

app.include_router(extract_routes, prefix="/extraction", tags=["Extraction d'Informations (IE)"])

app.include_router(scoring_routes, prefix="/scoring", tags=["Scoring & credit verification"])

app.include_router(evaluation_router, prefix="/evaluation_propriete", tags=["Évaluation de la Propriété"])

app.include_router(decision_routes, prefix="/decision", tags=["Request decision"])


def service_web_composite(mapper, connection, target):
    request_id = str(target.id)
    user_id = int(target.user_id)
    text = target.text
    url_to_extract_data = "http://127.0.0.1:8000/extraction/extract"
    payload_to_extract_data = {"request_id": request_id, "text": text}
    response_extract = requests.post(url_to_extract_data, json=payload_to_extract_data)
    response_extract_body = json.loads(response_extract.text)
    print('response_extract_body',response_extract_body, )
    if response_extract.status_code != 200:
        return
    url_to_evaluate_property = "http://127.0.0.1:8000/evaluation_propriete/evaluate"
    payload_to_evaluate_property= {
        "request_id": request_id,
        "description": response_extract_body.get("description_propriete")
    }
    print(payload_to_evaluate_property)
    response_evaluate_property = requests.post(url_to_evaluate_property, json=payload_to_evaluate_property)
    if response_evaluate_property.status_code != 200:
        return
    response_evaluate_property_body = json.loads(response_evaluate_property.text)
    market_value = response_evaluate_property_body["market_value"]
    inspection_report = response_evaluate_property_body["inspection_report"]
    legal_compliance = response_evaluate_property_body["legal_compliance"]
    url_to_get_user_scoring = "http://127.0.0.1:8000/scoring/scoring"
    payload_to_get_user_scoring = {
        "user_id": user_id
    }
    response_user_scoring = requests.post(url_to_get_user_scoring, json=payload_to_get_user_scoring)
    print(f"payload_to_get_user_scoring", response_user_scoring)

event.listen(DemandesInfo, 'after_insert', service_web_composite)