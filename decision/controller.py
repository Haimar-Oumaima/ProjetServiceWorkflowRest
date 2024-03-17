from decision.schemas import ScoringResponse, PropertyEvaluationResponse
from sqlalchemy.orm import Session
from extraction.model import ExtractedInfo

def get_extract_info_value(db: Session, request_id: int, column_name: str):
    # Query the extract_info table to get the value of the specified column for the given request_id
    result = db.query(ExtractedInfo).filter(ExtractedInfo.request_id == request_id).first()
    
    if result:
        if hasattr(result, column_name):
            return getattr(result, column_name)
    
    # Return None if the request_id or column_name is not found, or if the result is empty
    return None


def make_decision(db: Session,scoring_response: ScoringResponse, property_evaluation_response: PropertyEvaluationResponse):
    if scoring_response.eligibility_result.startswith("User is not eligible") or property_evaluation_response.inspection_report == "Problèmes potentiels détectés":
        return {
            "decision": "refused",
            "message": "Sorry, your request has been refused",
            "reason": "The user is not eligible or inspection detected problems"
        }
    else:
        request_id = property_evaluation_response.request_id
        
        requested_amount = float(get_extract_info_value(db, request_id=request_id , column_name="montant_pret"))
        loan_duration = float(get_extract_info_value(db, request_id=request_id , column_name="duree_pret"))
                
        # Calculate interest rate (10% of requested amount)
        interest_rate = requested_amount * 0.1
        
        # Calculate monthly amount
        monthly_amount = round((requested_amount + interest_rate) / (loan_duration * 12), 2)
        
        return {
            "decision": "approved",
            "message": "Congratulations, your request has been approved",
            "interest_rate": str(interest_rate) + " Euros",
            "monthly_amount": str(monthly_amount) + " Euros"        
            }
