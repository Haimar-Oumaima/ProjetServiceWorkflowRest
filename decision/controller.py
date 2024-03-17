import random
import re
from decision.model import Decision
from decision.schemas import ScoringResponse, PropertyEvaluationResponse
from sqlalchemy.orm import Session
from extraction.model import ExtractedInfo


def get_extract_info_value(db: Session, request_id: int):
    # Query the extract_info table to get the value of the specified column for the given request_id
    result = db.query(ExtractedInfo).filter(ExtractedInfo.request_id == request_id).first()
    return result


def make_decision(db: Session, scoring_response: ScoringResponse,
                  property_evaluation_response: PropertyEvaluationResponse):
    decision_payload = {
        "request_id": property_evaluation_response.request_id
    }
    if scoring_response.eligibility_result.startswith(
            "User is not eligible") or property_evaluation_response.inspection_report == "Problèmes potentiels détectés":
        decision_payload.update({
            "decision": "refused",
            "message": "Sorry, your request has been refused",
            "reason": "The user is not eligible or inspection detected problems"
        })
    else:
        request_id = property_evaluation_response.request_id
        extract_info = get_extract_info_value(db, request_id)
        requested_amount = getattr(extract_info, "montant_pret")
        loan_duration = convert_loan_duration(getattr(extract_info, "duree_pret"))
        if loan_duration is None:
            loan_duration = random.randint(1, 25)

        requested_amount = float(requested_amount)
        loan_duration = float(loan_duration)

        interest_rate = requested_amount * 0.1

        monthly_amount = round((requested_amount + interest_rate) / (loan_duration * 12), 2)

        decision_payload.update({
            "decision": "approved",
            "message": "Congratulations, your request has been approved",
            "interest_rate": str(interest_rate) + " Euros",
            "monthly_amount": str(monthly_amount) + " Euros"
        })
    decision = Decision(**decision_payload)
    db.add(decision)
    db.commit()
    db.refresh(decision)
    return decision


def convert_loan_duration(loan_duration):
    if isinstance(loan_duration, str):
        match = re.search(r'\d+', loan_duration)
        if match:
            return float(match.group())
        else:
            return None
    elif loan_duration is None:
        return float(random.randint(1, 25))
    else:
        return float(loan_duration)