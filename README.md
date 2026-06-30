# 🚆 Railway Management System

A simple full-stack Railway Management System built using **Flask**, **MySQL**, and **Streamlit**. This project was created to learn full-stack development, REST APIs, authentication, and database management.

## Features

* User Registration & Login
* JWT Authentication
* Admin and User Roles
* View Available Trains
* Book Train Tickets
* Automatic PNR Generation
* Seat Availability Check
* Prevents Double Booking

## Tech Stack

**Backend**

* Python
* Flask
* Flask-JWT-Extended

**Database**

* MySQL

**Frontend**

* Streamlit

## Project Structure

```text
railway-management-system/
│── backend/
│── frontend/
│── database/
│── requirements.txt
│── README.md
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/railway-management-system.git
cd railway-management-system
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Import the SQL file and update the database credentials in `backend/config.py`.

### Run the Backend

```bash
cd backend
python app.py
```

### Run the Frontend

```bash
cd frontend
streamlit run app.py
```

## Future Improvements

* Payment Integration
* PDF Ticket Generation
* Admin Dashboard
* Email Notifications
* Better UI

## Learning Outcomes

This project helped me understand:

* REST APIs
* JWT Authentication
* Password Hashing
* Database Design
* Full-Stack Development
* Role-Based Access Control
* Seat Booking Logic

This project was built as a learning project to practice backend development, database management, and frontend integration using Python.
