import re
from datetime import datetime,timezone
from database import users_collection

# Phần 1 : Data Validation : Xử lý Dữ liệu trước khi cho vào DB 
def validate_user(username, email, password):

    username = username.strip()            # Loại bỏ space ở đầu/cuối
    email = email.strip().lower()          # Email ko phân biệt viết hoa/ thường
 # Kiểm tra xem Username/Email/Password có bị trống ko 
    if not username:
        raise ValueError("Username is required")
    if not email:
        raise ValueError("Email is required")
    if not password : 
        raise ValueError("Password is required")
    
 # Kiểm tra độ dài Username có thỏa mãn ko
    if len(username) < 3 or len(username) > 20:
        raise ValueError("Username must be 3-20 characters")

 # Kiểm tra xem Username có chứa kí tự ko hợp lệ hay không
    username_pattern = r"^[a-zA-Z0-9_]+$"
    if not re.match(username_pattern, username):
        raise ValueError("Invalid Username")
 # Kiểm tra Email có đúng form hay không 
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        raise ValueError("Invalid Email Form")

 # Kiểm tra Email / Username đã tồn tại hay chưa.
    if users_collection.find_one({"email": email}):
        raise ValueError("Email already exists")

    if users_collection.find_one({"username": username}):
        raise ValueError("Username already exists")


# Phần 2 : Tạo người dùng mới
def create_user(username, email, password_hash):
    validate_user(username, email, password_hash)
    return {
        "username": username,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.now(timezone.utc)
    }

# Note : _id của 1 Collection luôn được tự động thêm, và nó thuộc kiểu dữ liệu ObjectID