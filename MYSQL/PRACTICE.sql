show databases;

# Creating Database
CREATE DATABASE college;

# Select The Database
USE college;

# Creating Table students
CREATE TABLE IF NOT EXISTS students(name varchar(50),age int,address varchar(100),marks int);

# Structure Of Table
DESC students;

# INSERTING VALUES IN TABLE
INSERT INTO students VALUES ('Abir',22,'Assam',100);
INSERT INTO students(name,age,address,marks) VALUES ('Amisha',20,'Assam',100);
INSERT INTO students VALUES ('Vikas',21,'Haryana',95),('Mukund',20,'Rajasthan',90),('Anam',21,'Telengana',98);

# Viewing The Data Of Table
SELECT * FROM students;

# View Students From Assam
SELECT * FROM students where address like 'Assam';

# Display students whose marks are greater than 75.
SELECT * FROM students WHERE marks>=95;

# Display students whose age is less than 21.
SELECT * FROM students WHERE marks<95;

# Display students who belong to Mumbai and scored more than 95
SELECT * FROM students WHERE marks>90 and address like 'Assam';

# Display students whose marks are between 60 and 90.
SELECT * FROM students WHERE marks between 95 and 100;

# Display students who belong to Delhi OR Pune.
SELECT * FROM students WHERE address like 'Assam' or address like 'Haryana';

# Display students whose age is NOT 22.
SELECT * FROM students WHERE age <> 22;

# Display students whose name starts with 'A'.
SELECT * FROM students WHERE name like 'A%';

# Display students whose name ends with 'n'.
SELECT * FROM students WHERE name like '%m'; # m -> M and m both

# Display students whose city is in (Delhi, Mumbai, Chandigarh).
SELECT * FROM students WHERE address like 'Assam' or address like 'Haryana';
