from flask import Blueprint, request, jsonify
from db import get_connection
from auth import hash_password, check_password
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (%s,%s,%s)",
        (data["username"], hash_password(data["password"]), data.get("role","user"))
    )

    conn.commit()
    return jsonify({"message": "User created"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT user_id, password_hash, role FROM users WHERE username=%s",
        (data["username"],)
    )

    user = cursor.fetchone()

    if user and check_password(data["password"], user[1]):
        token = create_access_token(identity={
            "user_id": user[0],
            "role": user[2]
        })
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401
