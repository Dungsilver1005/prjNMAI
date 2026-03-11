from datetime import datetime,timezone
from database import db  # import biến db từ file database  
import re 
    
def create_feedback(user_id, emotion_log_id, feedback_text, rating):

    feedback = {
        "user_id": user_id,
        "emotion_log_id": emotion_log_id,
        "feedback_text": feedback_text,
        "rating": rating,
        "created_at": datetime.now(timezone.utc)
    }

    return feedback