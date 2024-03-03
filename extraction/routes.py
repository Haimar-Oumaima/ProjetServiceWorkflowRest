from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db, get_token_from_header, get_user_from_token
from . import controller, schemas, model

# Création d'un nouvel objet APIRouter pour gérer les routes liées à l'extraction de texte
extract_routes = APIRouter()

# extract_text
    # Cette fonction est un endpoint qui réagit aux requêtes POST à l'adresse "/extract".
    # Elle attend une payload conforme au modèle défini dans `schemas.TextSchema`.

    # `db: Session = Depends(get_db)` utilise la fonction de dépendance `get_db` pour fournir
    # une session de base de données SQLAlchemy à l'endpoint. Cela permet de faire des opérations
    # sur la base de données dans le corps de la fonction.

    # `token: str = Depends(get_token_from_header)` utilise la fonction de dépendance
    # `get_token_from_header` pour extraire le token JWT de l'en-tête Authorization de la requête.
    # Ce token est ensuite utilisé pour identifier et authentifier l'utilisateur.

@extract_routes.post("/extract")
def extract_text(text_schema: schemas.TextSchema, db: Session = Depends(get_db)):
    try:
        result = controller.extract_information(text=text_schema.text,db=db, request_id=text_schema.request_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
