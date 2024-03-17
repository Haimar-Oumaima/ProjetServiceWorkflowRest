import json

import requests
from fastapi import FastAPI
from sqlalchemy import event
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy import update

import database
from decision.model import Decision
from decision.routes import decision_routes
from demandes.model import DemandesInfo
from evaluation.model import PropertyEvaluation
from evaluation.routes import evaluation_router
from extraction.model import ExtractedInfo
from register_login.model import User
from register_login.routes import auth_routes
from extraction.routes import extract_routes
from demandes.routes import requests_routes
from scoring.routes import scoring_routes

User.metadata.create_all(bind=database.engine)
ExtractedInfo.metadata.create_all(bind=database.engine)
DemandesInfo.metadata.create_all(bind=database.engine)
PropertyEvaluation.metadata.create_all(bind=database.engine)
Decision.metadata.create_all(bind=database.engine)

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_routes, prefix="/login_register", tags=["Register & Login"])

app.include_router(requests_routes, prefix="/requests", tags=["Extraction d'Informations (IE)"])

app.include_router(extract_routes, prefix="/extraction", tags=["Extraction d'Informations (IE)"])

app.include_router(scoring_routes, prefix="/scoring", tags=["Scoring & credit verification"])

app.include_router(evaluation_router, prefix="/evaluation_propriete", tags=["Évaluation de la Propriété"])

app.include_router(decision_routes, prefix="/decision", tags=["Request decision"])



def extract_data(target):
    request_id = str(target.id)
    text = target.text
    url_to_extract_data = "http://127.0.0.1:8000/extraction/extract"
    payload_to_extract_data = {"request_id": request_id, "text": text}
    print("Commencer la récupération des données d'extraction...")
    response_extract = requests.post(url_to_extract_data, json=payload_to_extract_data)
    print('response_extract_body', response_extract.text)
    response_extract_body = json.loads(response_extract.text)
    print('response_extract_body', response_extract_body)
    if response_extract.status_code != 200:
        print("Échec de la récupération des données d'extraction")
        return None
    print("Fin de la récupération des données d'extraction")
    return response_extract_body

def evaluate_property(response_extract_body):
    request_id = response_extract_body.get("request_id")
    description = response_extract_body.get("description_propriete")
    url_to_evaluate_property = "http://127.0.0.1:8000/evaluation_propriete/evaluate"
    payload_to_evaluate_property = {"request_id": request_id, "description": description}
    print("Commencer l'évaluation de la propriété...")
    print("payload_to_evaluate_property", payload_to_evaluate_property)
    response_evaluate_property = requests.post(url_to_evaluate_property, json=payload_to_evaluate_property)
    print('response_evaluate_property_body', response_evaluate_property.text)
    response_evaluate_property_body = json.loads(response_evaluate_property.text)
    if response_evaluate_property.status_code != 200:
        print("Échec de l'évaluation de la propriété")
        return None
    print("Fin de l'évaluation de la propriété")
    return response_evaluate_property_body

def get_user_scoring(user_id):
    url_to_get_user_scoring = "http://127.0.0.1:8000/scoring/scoring"
    payload_to_get_user_scoring = {"user_id": user_id}
    print("Commencer la récupération du scoring utilisateur...")
    response_user_scoring = requests.post(url_to_get_user_scoring, json=payload_to_get_user_scoring)
    print('response_user_scoring_body', response_user_scoring.text)
    response_user_scoring_body = json.loads(response_user_scoring.text)
    print("Fin de la récupération du scoring utilisateur")
    return response_user_scoring_body

def make_decision(scoring_response, property_evaluation_response):
    url_to_make_decision = "http://127.0.0.1:8000/decision/decide"
    payload_to_make_decision = {"scoring_response": scoring_response, "property_evaluation_response": property_evaluation_response}
    print("Commencer à prendre une décision...")
    print("payload_to_make_decision", payload_to_make_decision)
    response_decision = requests.post(url_to_make_decision, json=payload_to_make_decision)
    print(f"response_decision", response_decision.text)
    print("Fin de la prise de décision")
    return response_decision


def service_web_composite(mapper, connection, target):
    print("Insertion dans la base de données:", target)
    response_extract_body = extract_data(target)
    if response_extract_body is None:
        print("Erreur lors de l'extraction des données")
        return

    response_evaluate_property_body = evaluate_property(response_extract_body)
    if response_evaluate_property_body is None:
        print("Erreur lors de l'évaluation de la propriété")
        return

    user_id = target.user_id
    response_user_scoring_body = get_user_scoring(user_id)

    decision_response = make_decision(response_user_scoring_body, response_evaluate_property_body)
    print("Décision prise:", decision_response.text)

event.listen(DemandesInfo, 'after_insert', service_web_composite)