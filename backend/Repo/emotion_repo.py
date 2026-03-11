from database import emotion_collection
from datetime import datetime, timedelta, timezone
from bson import ObjectId


# Thêm emotion log mới
def insert_emotion_log(emotion_log):
    result = emotion_collection.insert_one(emotion_log)
    return result.inserted_id

# Lấy emotion log theo emotion_id
def get_emotion_by_id(emotion_id):
    return emotion_collection.find_one({"_id": ObjectId(emotion_id)})


# Lấy tất cả emotion log của 1 user
def get_emotions_by_user(user_id):
    return list(emotion_collection.find({"user_id": ObjectId(user_id)}))


# Lấy emotion gần nhất của user
def get_latest_emotion(user_id):
    return emotion_collection.find_one(
        {"user_id":ObjectId(user_id)},
        sort=[("created_at", -1)]
    )

# Lấy ra emotion của 7 ngày gần nhất 
def get_emotions_last_7_days(user_id):
    seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
    emotions = emotion_collection.find({
        "user_id": ObjectId(user_id),
        "created_at": {"$gte": seven_days_ago}
    }).sort([("created_at", 1)])
    return list(emotions)

# Xóa emotion log
def delete_emotion(emotion_id):
    return emotion_collection.delete_one({"_id": ObjectId(emotion_id)})