**🚆 Railway Management System**

A simple full-stack Railway Management System built using Flask, MySQL, and Streamlit. This project was created to learn full-stack development, REST APIs, authentication, and database management.

**Features**
User Registration & Login
JWT Authentication
Admin and User Roles
View Available Trains
Book Train Tickets
Automatic PNR Generation
Seat Availability Check
Prevents Double Booking
Tech Stack

**Backend**

Python
Flask
Flask-JWT-Extended

**Database**

MySQL

**Frontend**

Streamlit
Project Structure
railway-management-system/
│── backend/
│── frontend/
│── database/
│── requirements.txt
│── README.md
Getting Started
Clone the repository
git clone https://github.com/Shwetarawat061/railway-management-system.git
cd railway-management-system
Create a virtual environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Configure MySQL

Import the SQL file and update the database credentials in backend/config.py.

Run the Backend
cd backend
python app.py
Run the Frontend
cd frontend
streamlit run app.py
Future Improvements
Payment Integration
PDF Ticket Generation
Admin Dashboard
Email Notifications
Better UI
Learning Outcomes

**This project helped me understand:**

REST APIs
JWT Authentication
Password Hashing
Database Design
Full-Stack Development
Role-Based Access Control
Seat Booking Logic

This project was built as a learning project to practice backend development, database management, and frontend integration using Python.
