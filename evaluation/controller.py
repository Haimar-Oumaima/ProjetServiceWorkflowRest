import random
from sqlalchemy.orm import Session

from evaluation.model import PropertyEvaluation


def evaluate_property_value(db: Session, description, request_id: int):
    # Analyse des données du marché immobilier
    market_value = analyze_real_estate_data(description)
    # Inspection virtuelle ou sur place
    inspection_report = perform_property_inspection(description)

    # Conformité légale et réglementaire
    legal_compliance = check_legal_compliance(description)

    # Compilation du rapport d'évaluation
    evaluation_report = {
        "market_value": market_value,
        "inspection_report": inspection_report["resultat"],
        "legal_compliance": legal_compliance,
        "request_id": request_id
    }
    # return evaluation_report
    evaluation_info  = PropertyEvaluation(**evaluation_report)
    # Ajouter l'instance à la session
    db.add(evaluation_info)

    # Commit pour enregistrer les changements dans la base de données
    db.commit()

    # Rafraîchir l'objet pour s'assurer qu'il contient les dernières données de la base de données
    db.refresh(evaluation_info)

    return evaluation_info

def analyze_real_estate_data(description):
    # Valeur de base pour la propriété
    base_value = random.randint(100000, 1000000)

    # Ajustements basés sur des mots-clés dans la description
    if 'deux étages' in description:
        base_value *= 1.2
    if 'jardin' in description:
        base_value *= 1.15
    if 'quartier résidentiel calme' in description:
        base_value *= 1.1

    # Retourner la valeur estimée arrondie à l'entier le plus proche
    estimated_value = round(base_value)
    return estimated_value

def check_legal_compliance(description):
    # Probabilité de base de conformité
    compliance_probability = 0.9  # 90% de chance que la propriété soit conforme

    # Rechercher des mots clés qui pourraient indiquer des problèmes
    if any(keyword in description for keyword in ["litige", "non conforme", "sanction"]):
        compliance_probability -= 0.5  # Réduire la probabilité de conformité

    # Simuler le résultat de la vérification de conformité basé sur la probabilité ajustée
    is_compliant = random.random() < compliance_probability
    return is_compliant

def perform_property_inspection(property_details):
    inspection_type = random.choice(['virtuelle', 'sur place'])
    if inspection_type == 'virtuelle':
        inspection_result = _virtual_inspection(property_details)
    else:
        inspection_result = _on_site_inspection(property_details)

    return {
        'type_inspection': inspection_type,
        'resultat': inspection_result
    }

def _virtual_inspection(property_details):
    has_issues = random.choice([True, False])
    return 'Pas de problèmes détectés' if not has_issues else 'Problèmes potentiels détectés'

def _on_site_inspection(property_details):
    has_major_issues = random.choice([True, False])
    return 'Propriété en excellent état' if not has_major_issues else 'Réparations majeures nécessaires'



