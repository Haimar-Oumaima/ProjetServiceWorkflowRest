from sqlalchemy.orm import Session
from .model import UserHistory

def get_user_history(db: Session, user_id: int):
    return db.query(UserHistory).filter(UserHistory.user_id == user_id).first()

def calculate_score(db: Session, user_id: int):
    user_history = get_user_history(db, user_id)

    if user_history is None:
        return "Client history not found."

    # Perform score calculation based on user history
    score = 0

    if user_history.debts == 0:
        score += 2

    if user_history.late_payments < 3:
        score += 1

    if user_history.bankruptcy == 0:
        score += 3

    if user_history.monthly_expenses > 0:
        ratio_revenu_depenses = user_history.monthly_revenue / user_history.monthly_expenses

        if ratio_revenu_depenses >= 2.0:
            score += 4

    return score
