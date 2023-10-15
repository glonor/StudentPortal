-- Create a new database for student records
CREATE DATABASE student_records;

-- Switch to the 'student_records' database
USE student_records;

-- Create a table for student information
CREATE TABLE students (
  StudentID INT AUTO_INCREMENT PRIMARY KEY,
  FirstName VARCHAR(50),
  LastName VARCHAR(50),
  Major VARCHAR(50),
  AverageGrade DECIMAL(4, 2)
);

-- Insert sample student data
INSERT INTO students
  (FirstName, LastName, Major, AverageGrade)
VALUES
  ('Luca', 'Rossi', 'Computer Science', 28.75),
  ('Sofia', 'Bianchi', 'Engineering', 29.25),
  ('Marco', 'Moretti', 'Business Administration', 30.00),
  ('Elena', 'Ricci', 'Biology', 27.50);
