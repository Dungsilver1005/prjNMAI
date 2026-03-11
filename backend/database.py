from pymongo import MongoClient
import certifi

# URI kết nối của bạn
uri = "mongodb+srv://tuanhungnguyenvan01042006_db_user:oCMPtfbVsP7T7LTs@emoaicluster.fj0zt5h.mongodb.net/?appName=EmoAICluster"

try:
    # 1. Khởi tạo kết nối với chứng chỉ bảo mật và timeout 5 giây
    client = MongoClient(uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)
    
    # 2. Kiểm tra kết nối thật sự bằng lệnh ping
    client.admin.command('ping')
    print("✅ Kết nối thành công tới MongoDB Atlas!")

    # 3. Khởi tạo Database tên là 'emotion_ai_db'
    db = client["emotion_ai_db"]

    # 4. Khởi tạo 3 Collection lần lượt là users, emotion, feedback
    users_collection = db["users"]
    emotion_collection = db["emotion"]
    feedback_collection = db["feedback"]

    print(f" Đã khởi tạo database: {db.name}")
    print(f" Đã sẵn sàng 3 collections: {['users', 'emotion', 'feedback']}")

except Exception as e:
    print(f" Kết nối thất bại! Lý do: {e}")