CREATE DATABASE railway_management;
USE railway_management;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('admin','user') DEFAULT 'user'
);

CREATE TABLE train_info (
    train_id INT AUTO_INCREMENT PRIMARY KEY,
    train_name VARCHAR(100),
    train_type VARCHAR(50),
    total_coaches INT,
    source VARCHAR(100),
    destination VARCHAR(100),
    departure_time TIME,
    arrival_time TIME
);

CREATE TABLE booking_record (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT,
    train_id INT,
    booking_date DATE,
    seat_no VARCHAR(10),
    coach_no VARCHAR(10),
    status ENUM('Booked','Cancelled') DEFAULT 'Booked',
    pnr VARCHAR(30) UNIQUE,
    UNIQUE KEY unique_seat (train_id, seat_no, coach_no, booking_date)
);
