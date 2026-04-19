CREATE DATABASE hospital_db;
USE hospital_db;
CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    contact VARCHAR(15),
    address TEXT,
    disease VARCHAR(100)
);
SHOW TABLES;
SELECT * FROM patients;
