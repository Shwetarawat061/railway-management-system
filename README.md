# 🚆 Railway Management System (Full Stack Project)

A full-stack Railway Management System built using **Flask (Python backend)**, **MySQL database**, and a **Streamlit-based Python UI frontend**.

This project demonstrates real-world concepts like:
- Role-based authentication (Admin/User)
- Secure password hashing (bcrypt)
- Seat booking with locking (no double booking)
- PNR generation system
- REST API architecture
- Full-stack integration

---

# 📌 Features

## 👤 Authentication
- User registration & login
- JWT-based secure authentication
- Role-based access (Admin / User)

## 🚉 Train Management
- View all available trains
- Admin can manage train data

## 🎟️ Booking System
- Book train tickets
- Automatic seat availability check
- Prevents double booking (database-level locking)
- Generates unique PNR for every booking

## 🔐 Security
- Password hashing using bcrypt
- JWT token authentication
- Role-based API access control

---

# 🏗️ Tech Stack

### Backend:
- Python
- Flask
- Flask-JWT-Extended

### Database:
- MySQL

### Frontend:
- Streamlit (Python UI)

---

# 📁 Project Structure
railway-management-system/
│
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── db.py
│ ├── auth.py
│ ├── utils.py
│ ├── routes/
│ └── models/
│
├── frontend/
│ └── app.py
│
├── requirements.txt
└── README.md
---

# ⚙️ Setup Instructions

## 1. Clone the repository
```bash
git clone https://github.com/your-username/railway-management-system.git
cd railway-management-system
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Setup MySQL database

Run the SQL file located in:

backend/models/init_db.sql
5. Configure database credentials

Update:

backend/config.py
6. Run backend server
cd backend
python app.py

Backend runs at:

http://127.0.0.1:5000
7. Run frontend (Streamlit UI)
cd frontend
streamlit run app.py

Frontend runs at:

http://localhost:8501
🔄 System Architecture
Frontend (Streamlit)
        ↓
Flask REST API
        ↓
MySQL Database
