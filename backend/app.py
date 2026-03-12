import os
from flask import Flask, request, jsonify, session, render_template, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from security import hash_password, verify_password, login_required
from database import users_collection, emotion_collection, db
from Collection.user_model import create_user
from Collection.emotion_model import create_emotion_log
from Repo.user_repo import insert_user, get_user_by_email, get_user_by_id
from Repo.emotion_repo import insert_emotion_log

# Setup paths relative to backend directory
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '..', 'frontend', 'templates')
static_dir = os.path.join(base_dir, '..', 'frontend', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.getenv("SECRET_KEY", "super_secret_key_change_in_production")


# ─── ROUTES ───────────────────────────────────────────────

@app.route('/')
def index():
    if session.get("user_id"):
        return redirect(url_for('chat_page'))
    return redirect(url_for('login_page'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '')

    user = get_user_by_email(email)
    if not user or not verify_password(password, user['password_hash']):
        return render_template('login.html', error="Email hoặc Password không chính xác")

    session["user_id"] = str(user["_id"])
    session["username"] = user["username"]
    return redirect(url_for('chat_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'GET':
        return render_template('register.html')

    username = request.form.get('username', '').strip()
    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '')

    if not username or not email or not password:
        return render_template('register.html', error="Vui lòng nhập đầy đủ thông tin.")

    try:
        pw_hash = hash_password(password)
        user_doc = create_user(username, email, pw_hash)
        user_id = insert_user(user_doc)

        session["user_id"] = str(user_id)
        session["username"] = username
        return redirect(url_for('chat_page'))
    except ValueError as e:
        return render_template('register.html', error=str(e))
    except Exception as e:
        print(f"[Register Error] {type(e).__name__}: {e}")
        return render_template('register.html', error="Đã xảy ra lỗi, vui lòng thử lại.")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))


@app.route('/chat')
@login_required
def chat_page():
    return render_template('chat.html', username=session.get("username", "Guest"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)