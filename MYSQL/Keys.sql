
CREATE DATABASE company;
USE company;

# Q1. Create a table employees with emp_id as a unique identifier that cannot be NULL.
CREATE TABLE employees(emp_id INT PRIMARY KEY);

# Q2. Create a table departments with dept_id and ensure it uniquely identifies each record
CREATE TABLE departments (dept_id INT PRIMARY KEY);

# Q3. Create a table students where student_id uniquely identifies each student and cannot be duplicated.
CREATE TABLE students (student_id INT PRIMARY KEY);

# Q4. Create two tables customers and orders where each order must belong to an existing customer.
CREATE TABLE customers (customer_id INT PRIMARY KEY);

CREATE TABLE orders (order_id INT PRIMARY KEY,customer_id INT NOT NULL,
FOREIGN KEY (customer_id) REFERENCES customers(customer_id));

# Q5. Create two tables authors and books so that if an author is deleted, all their books are automatically removed.
CREATE TABLE authors (author_id INT PRIMARY KEY);

CREATE TABLE books (book_id INT PRIMARY KEY,author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

