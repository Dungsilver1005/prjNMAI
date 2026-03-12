from functools import wraps
from flask import abort, redirect, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    return generate_password_hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    if isinstance(password_hash, bytes):
        password_hash = password_hash.decode('utf-8')
    return check_password_hash(password_hash, password)

def login_required(view_func):
    """
    Decorator kiểm tra session. Nếu chưa đăng nhập, chuyển hướng về trang login.
    Đối với các API Endpoint, trả về lỗi 401.
    """
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            if request.path.startswith("/api/"):
                abort(401)
            return redirect(url_for("login_page"))
        return view_func(*args, **kwargs)
    return wrapper
