import json

import spacy
from .model import ExtractedInfo
from sqlalchemy.orm import Session
from ia.extract import ExtractIa

nlp = spacy.load("en_core_web_sm")

def extract_information(text: str, db: Session, user_id: int):

    # Initialiser une instance de la classe ExtractIa pour traiter le texte
    ExtractData =  ExtractIa()

    # Préparer le texte en le nettoyant ou en effectuant d'autres prétraitements nécessaires
    prepared_text = ExtractData.prepare_text(text_to_prepare=text)

    # Analyser le texte préparé pour en extraire des caractéristiques ou des informations pertinentes
    analysed_text = ExtractData.analyse_text(text_to_analyse=prepared_text)

    # Extraire des informations spécifiques du texte analysé, retournées sous forme de chaîne JSON
    extracted_info_str = ExtractData.extract_info(info_to_extract=analysed_text)

    # Convertir la chaîne JSON en un dictionnaire
    extracted_info = json.loads(extracted_info_str)

    # Mettre à jour le dictionnaire avec l'ID de l'utilisateur, ajoutant cette information aux données extraites
    extracted_info.update({
        "user_id":user_id
    })

    # Afficher dans la console l'ID de l'utilisateur et les informations extraites pour dbg
    print(f"hey  {user_id, extracted_info} ")

    # Créer une instance du modèle ExtractedInfo en déballant le dictionnaire des informations extraites
    info_instance = ExtractedInfo(**extracted_info)

    # Ajouter l'instance à la session
    db.add(info_instance)

    # Commit pour enregistrer les changements dans la base de données
    db.commit()

    # Rafraîchir l'objet pour s'assurer qu'il contient les dernières données de la base de données
    db.refresh(info_instance)

    return info_instance