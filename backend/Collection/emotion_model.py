from datetime import datetime,timezone

def create_emotion_log(user_id, emotion_id, emotion, confidence, image_base64):
    emotion_log = {
        "user_id": user_id,
        "emotion_id": emotion_id,
        "emotion": emotion,
        "confidence": confidence,
        "image_base64": image_base64,
        "created_at": datetime.now(timezone.utc)
    }
    return emotion_log