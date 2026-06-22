import streamlit as st
import requests

API = "http://127.0.0.1:5000"

st.title("🚆 Railway Management System")

menu = st.sidebar.selectbox("Menu", ["Login", "Register", "Book Ticket", "View Trains"])

token = None

# ---------------- LOGIN ----------------
if menu == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(API+"/auth/login", json={
            "username": username,
            "password": password
        })

        if res.status_code == 200:
            token = res.json()["token"]
            st.success("Login successful")
            st.session_state["token"] = token
        else:
            st.error("Login failed")

# ---------------- REGISTER ----------------
elif menu == "Register":
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Register"):
        requests.post(API+"/auth/register", json={
            "username": u,
            "password": p
        })
        st.success("User created")

# ---------------- VIEW TRAINS ----------------
elif menu == "View Trains":
    if "token" in st.session_state:
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        res = requests.get(API+"/train/", headers=headers)
        st.write(res.json())
    else:
        st.warning("Login first")

# ---------------- BOOK TICKET ----------------
elif menu == "Book Ticket":
    if "token" in st.session_state:
        train_id = st.text_input("Train ID")
        seat = st.text_input("Seat No")
        coach = st.text_input("Coach No")
        date = st.text_input("Date (YYYY-MM-DD)")

        if st.button("Book"):
            headers = {"Authorization": f"Bearer {st.session_state['token']}"}
            res = requests.post(API+"/booking/book",
                json={
                    "train_id": train_id,
                    "seat_no": seat,
                    "coach_no": coach,
                    "date": date
                },
                headers=headers
            )

            st.write(res.json())
    else:
        st.warning("Login first")
