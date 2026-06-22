from flask import Blueprint, jsonify
from db import get_connection
from flask_jwt_extended import jwt_required

train_bp = Blueprint("train", __name__)

@train_bp.route("/", methods=["GET"])
@jwt_required()
def get_trains():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM train_info")
    return jsonify(cursor.fetchall())
