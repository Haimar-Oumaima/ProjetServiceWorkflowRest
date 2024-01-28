import json

import spacy
from .model import ExtractedInfo
from sqlalchemy.orm import Session
from ia.extract import ExtractIa

nlp = spacy.load("en_core_web_sm")

def extract_information(text: str, db: Session):
    ExtractData =  ExtractIa()
    prepared_text = ExtractData.prepare_text(text_to_prepare=text)
    analysed_text = ExtractData.analyse_text(text_to_analyse=prepared_text)
    extracted_info_str = ExtractData.extract_info(info_to_extract=analysed_text)

    # Convertir la chaîne JSON en un dictionnaire
    extracted_info = json.loads(extracted_info_str)

    # Créer une instance de ExtractedInfo avec les données extraites
    info_instance = ExtractedInfo(**extracted_info)

    # Ajouter l'instance à la session
    db.add(info_instance)

    # Commit pour enregistrer les changements dans la base de données
    db.commit()

    # Rafraîchir l'objet pour s'assurer qu'il contient les dernières données de la base de données
    db.refresh(info_instance)

    return info_instance

    # doc = nlp(text)
    # extracted_info = ExtractedInfo(
    #     text=text,
    #     names=", ".join(ent.text for ent in doc.ents if ent.label_ == "PERSON"),
    #     addresses=", ".join(ent.text for ent in doc.ents if ent.label_ == "GPE"),
    #     dates=", ".join(ent.text for ent in doc.ents if ent.label_ == "DATE"),
    #     organizations=", ".join(ent.text for ent in doc.ents if ent.label_ == "ORG"),
    #     money=", ".join(ent.text for ent in doc.ents if ent.label_ == "MONEY"),
    #     keywords=""
    # )
    # db.add(extracted_info)
    # db.commit()
    # db.refresh(extracted_info)
    # return extracted_info
