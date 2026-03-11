from database import users_collection
from bson import ObjectId


def insert_user(user):
    result = users_collection.insert_one(user)
    return result.inserted_id


def get_user_by_email(email):
    return users_collection.find_one({"email": email})


def get_user_by_id(user_id):
    return users_collection.find_one({"_id": ObjectId(user_id)})


def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count