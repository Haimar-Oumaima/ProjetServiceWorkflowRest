# extraction_info/controller.py
import spacy

nlp = spacy.load("en_core_web_sm")  # Ou le modèle de votre choix

def preprocess_text(text):
    # Supprimer le bruit, normaliser, etc.
    return text

def extract_information(text):
    processed_text = preprocess_text(text)
    doc = nlp(processed_text)

    extracted_info = {
        "names": [ent.text for ent in doc.ents if ent.label_ == "PERSON"],
        "addresses": [ent.text for ent in doc.ents if ent.label_ == "GPE"],
        "dates": [ent.text for ent in doc.ents if ent.label_ == "DATE"],
        "organizations": [ent.text for ent in doc.ents if ent.label_ == "ORG"],
        "money": [ent.text for ent in doc.ents if ent.label_ == "MONEY"],
        # Ajoutez plus de catégories selon vos besoins
    }

    # Exemple d'extraction de phrases clés ou de mots-clés
    # Vous pouvez utiliser des techniques comme TF-IDF ou des modèles de langage pour extraire des mots-clés
    # ...

    return extracted_info
