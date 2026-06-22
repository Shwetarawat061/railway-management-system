#PNR+Seat Logic
import random
from datetime import datetime

def generate_pnr(train_id):
    return f"{datetime.now().strftime('%Y%m%d')}-{train_id}-{random.randint(1000,9999)}"


def is_seat_available(cursor, train_id, seat_no, coach_no, date):
    cursor.execute("""
        SELECT COUNT(*) FROM booking_record
        WHERE train_id=%s AND seat_no=%s AND coach_no=%s
        AND booking_date=%s AND status='Booked'
    """, (train_id, seat_no, coach_no, date))

    return cursor.fetchone()[0] == 0
