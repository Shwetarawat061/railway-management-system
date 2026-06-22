from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db import get_connection
from utils import generate_pnr, is_seat_available

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/book", methods=["POST"])
@jwt_required()
def book():
    data = request.json
    user = get_jwt_identity()

    conn = get_connection()
    cursor = conn.cursor()

    if not is_seat_available(cursor, data["train_id"], data["seat_no"], data["coach_no"], data["date"]):
        return jsonify({"error": "Seat already booked"}), 409

    pnr = generate_pnr(data["train_id"])

    cursor.execute("""
        INSERT INTO booking_record
        (passenger_id, train_id, booking_date, seat_no, coach_no, status, pnr)
        VALUES (%s,%s,%s,%s,%s,'Booked',%s)
    """, (
        user["user_id"],
        data["train_id"],
        data["date"],
        data["seat_no"],
        data["coach_no"],
        pnr
    ))

    conn.commit()

    return jsonify({"message": "Booked", "pnr": pnr})booking
