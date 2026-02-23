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

# Display first 3 students from table
SELECT * FROM students LIMIT 3;

# Display top 3 student who scored highest marks
SELECT * FROM students ORDER BY marks DESC LIMIT 3;

# Display 2 students after skipping first 2 records.
SELECT * FROM students LIMIT 2 OFFSET 2;

# Display only 1 student with lowest marks.
SELECT * FROM students order by marks LIMIT 1;

# Display first 4 students from Mumbai.
SELECT * FROM students WHERE address like 'ASSAM' LIMIT 1;

# Display all students sorted by marks ascending
SELECT * FROM students ORDER BY marks;

# Display all students sorted by marks descending
SELECT * FROM students ORDER BY marks DESC;

# Display studynts sorted by name alphabeticålly.
SELECT * FROM students ORDER BY name;

# Display students sorted by city then marks descending
SELECT * FROM students ORDER BY address ASC, marks DESC;

# Display students sorted by age descending
SELECT * FROM students ORDER BY age DESC;

# Find the total number of students.
SELECT COUNT(*) FROM students;

# Find the maximum marks scored.
SELECT MAX(marks) FROM students;

# Find the minimum marks scored.
SELECT MIN(marks) FROM students;

# Find the average marks of students.
SELECT AVG(marks) FROM students;

# Find the sum of all marks.
SELECT SUM(marks) FROM students;

# Count students age-wise.
SELECT age,count(*) FROM students GROUP BY age ORDER BY age;

# Show cities having more than 1 student.
SELECT address,COUNT(*) FROM students GROUP BY address HAVING COUNT(*) > 1;

# Show cities where average marks is greater than 80.
SELECT address, AVG(marks) FROM students GROUP BY address HAVING AVG(marks) > 80;

# Show age groups having total marks more than 80.
SELECT age, AVG(marks) FROM students GROUP BY age HAVING AVG(marks) > 80;

# 44 Show cities where maximum marks is 90
SELECT address,MAX(marks) FROM students GROUP BY address HAVING MAX(marks) = 90;

# Update marks of Mukund to 95
SET SQL_SAFE_UPDATES = 0;
UPDATE students SET marks = 95 WHERE name = 'Mukund';
SELECT * FROM students;

# Update city of Rahul to Mumbai.
UPDATE students SET address = 'UP' WHERE name = 'Vikas';

# Increase marks by 5 for students from Delhi.
UPDATE students SET marks = marks + 1 WHERE address = 'Telengana';

# Update age to 22 where name is Vikas.
UPDATE students SET age = 22 WHERE name = 'Vikas';

# Update marks to 100 where city is Assam.
UPDATE students SET marks = 100 WHERE address = 'Assam';

# Delete student amed Kunal.
INSERT INTO students VALUES('Kunal',20,'Mumbai',99);
DELETE FROM students WHERE name = 'Kunal';

# Delete marks less than 65.
DELETE FROM students WHERE marks < 65;

# Delete students from Chandigarh.
INSERT INTO students VALUES('Kunal',20,'Chandigarh',99);
DELETE FROM students WHERE address = 'Chandigarh';

# Delete students whose age is greater than 23.
INSERT INTO students VALUES('Kunal',23,'Chandigarh',99);
DELETE FROM students WHERE age > 22;
