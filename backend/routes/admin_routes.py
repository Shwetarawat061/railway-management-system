from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from db import get_connection

admin_bp = Blueprint("admin", __name__)


def admin_required():
    user = get_jwt_identity()

    if user["role"] != "admin":
        return None

    return user


# -----------------------------------
# Add Train
# -----------------------------------
@admin_bp.route("/train", methods=["POST"])
@jwt_required()
def add_train():

    if not admin_required():
        return jsonify({"message": "Access denied"}), 403

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO train_info
        (
            train_name,
            train_type,
            total_coaches,
            source,
            destination,
            departure_time,
            arrival_time
        )

        VALUES (%s,%s,%s,%s,%s,%s,%s)

    """,
    (
        data["train_name"],
        data["train_type"],
        data["total_coaches"],
        data["source"],
        data["destination"],
        data["departure_time"],
        data["arrival_time"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Train added successfully"})

@admin_bp.route("/train/<int:train_id>", methods=["PUT"])
@jwt_required()
def update_train(train_id):

    if not admin_required():
        return jsonify({"message": "Access denied"}), 403

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE train_info

        SET
        train_name=%s,
        train_type=%s,
        total_coaches=%s,
        source=%s,
        destination=%s,
        departure_time=%s,
        arrival_time=%s

        WHERE train_id=%s
    """,
    (
        data["train_name"],
        data["train_type"],
        data["total_coaches"],
        data["source"],
        data["destination"],
        data["departure_time"],
        data["arrival_time"],
        train_id
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Train updated"})

@admin_bp.route("/train/<int:train_id>", methods=["DELETE"])
@jwt_required()
def delete_train(train_id):

    if not admin_required():
        return jsonify({"message": "Access denied"}), 403

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM train_info WHERE train_id=%s",
        (train_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Train deleted"})

@admin_bp.route("/bookings", methods=["GET"])
@jwt_required()
def view_bookings():

    if not admin_required():
        return jsonify({"message": "Access denied"}), 403

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""

    SELECT

    b.booking_id,
    b.pnr,
    b.booking_date,
    b.seat_no,
    b.coach_no,
    b.status,

    t.train_name,

    u.username

    FROM booking_record b

    JOIN train_info t
    ON b.train_id=t.train_id

    JOIN users u
    ON b.passenger_id=u.user_id

    """)

    bookings = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(bookings)
