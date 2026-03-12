import os
import sys
from pymongo import MongoClient
import certifi
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Lấy URI kết nối MongoDB
uri = os.getenv("MONGO_URI")

if not uri:
    print("❌ MONGO_URI chưa được cấu hình trong file .env!")
    print("   Vui lòng tạo file .env với nội dung: MONGO_URI=mongodb+srv://...")
    sys.exit(1)

# Khởi tạo kết nối MongoDB với chứng chỉ SSL
client = MongoClient(
    uri,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=10000,
    connectTimeoutMS=10000,
    socketTimeoutMS=20000,
)

# Kiểm tra kết nối
try:
    client.admin.command("ping")
    print("✅ Kết nối thành công tới MongoDB Atlas!")
except Exception as e:
    print(f"❌ Không thể kết nối MongoDB Atlas: {e}")
    sys.exit(1)

# Khởi tạo Database và Collections
db = client["emotion_ai_db"]
users_collection = db["users"]
emotion_collection = db["emotion"]
feedback_collection = db["feedback"]

print(f"📦 Database: {db.name}")
print(f"📂 Collections: users, emotion, feedback")