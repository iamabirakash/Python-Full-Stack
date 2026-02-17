Microsoft Windows [Version 10.0.19045.6466]
(c) Microsoft Corporation. All rights reserved.

C:\Users\ABIR AKASH>mysql -u root -p
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 14
Server version: 8.0.45 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> ^C
mysql> exit()
    ->
    ->
    -> exit
    -> help
    -> \h

For information about MySQL products and services, visit:
   http://www.mysql.com/
For developer information, including the MySQL Reference Manual, visit:
   http://dev.mysql.com/
To buy MySQL Enterprise support, training, or other products, visit:
   https://shop.mysql.com/

List of all MySQL commands:
Note that all text commands must be first on line and end with ';'
?         (\?) Synonym for `help'.
clear     (\c) Clear the current input statement.
connect   (\r) Reconnect to the server. Optional arguments are db and host.
delimiter (\d) Set statement delimiter.
ego       (\G) Send command to mysql server, display result vertically.
exit      (\q) Exit mysql. Same as quit.
go        (\g) Send command to mysql server.
help      (\h) Display this help.
notee     (\t) Don't write into outfile.
print     (\p) Print current command.
prompt    (\R) Change your mysql prompt.
quit      (\q) Quit mysql.
rehash    (\#) Rebuild completion hash.
source    (\.) Execute an SQL script file. Takes a file name as an argument.
status    (\s) Get status information from the server.
system    (\!) Execute a system shell command, if enabled
tee       (\T) Set outfile [to_outfile]. Append everything into given outfile.
use       (\u) Use another database. Takes database name as argument.
charset   (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets.
warnings  (\W) Show warnings after every statement.
nowarning (\w) Don't show warnings after every statement.
resetconnection(\x) Clean session context.
query_attributes Sets string parameters (name1 value1 name2 value2 ...) for the next query to pick up.
ssl_session_data_print Serializes the current SSL session data to stdout or file

For server side help, type 'help contents'

    -> \q
Bye

C:\Users\ABIR AKASH>mysql --version
mysql  Ver 8.0.45 for Win64 on x86_64 (MySQL Community Server - GPL)

C:\Users\ABIR AKASH>mysql -u root -p
Enter password: ****
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.45 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| lpu                |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)

mysql> create database lpu2;
Query OK, 1 row affected (0.05 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| lpu                |
| lpu2               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql> use lpu2;
Database changed
mysql> show tables;
Empty set (0.01 sec)

mysql> CREATE TABLE student()
    -> CREATE TABLE student(id INT PRIMARY_KEY, name VARCHAR(50), age INT);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')
CREATE TABLE student(id INT PRIMARY_KEY, name VARCHAR(50), age INT)' at line 1
mysql> CREATE TABLE student(id INT PRIMARY KEY, name VARCHAR(50), age INT);
Query OK, 0 rows affected (0.07 sec)

mysql> show tables;
+----------------+
| Tables_in_lpu2 |
+----------------+
| student        |
+----------------+
1 row in set (0.00 sec)

mysql> DESC studentl
    -> DESC student;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DESC student' at line 2
mysql> DESC student;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | NO   | PRI | NULL    |       |
| name  | varchar(50) | YES  |     | NULL    |       |
| age   | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.05 sec)

mysql> INSERT INTO student VALUES(1,'Abir',22);
Query OK, 1 row affected (0.04 sec)

mysql> INSERT INTO student VALUES
    -> (2, 'Rahul', 21),
    -> (3, 'Amit', 22);
Query OK, 2 rows affected (0.05 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM student;
+----+-------+------+
| id | name  | age  |
+----+-------+------+
|  1 | Abir  |   22 |
|  2 | Rahul |   21 |
|  3 | Amit  |   22 |
+----+-------+------+
3 rows in set (0.00 sec)

mysql> SELECT name, age FROM student;
+-------+------+
| name  | age  |
+-------+------+
| Abir  |   22 |
| Rahul |   21 |
| Amit  |   22 |
+-------+------+
3 rows in set (0.00 sec)

mysql> DELETE from student where id=2;
Query OK, 1 row affected (0.05 sec)

mysql> SELECT * FROM student;
+----+------+------+
| id | name | age  |
+----+------+------+
|  1 | Abir |   22 |
|  3 | Amit |   22 |
+----+------+------+
2 rows in set (0.00 sec)

mysql> INSERT INTO student VALUES(2,'Manikant',21);
Query OK, 1 row affected (0.04 sec)

mysql> SELECT * FROM student;
+----+----------+------+
| id | name     | age  |
+----+----------+------+
|  1 | Abir     |   22 |
|  2 | Manikant |   21 |
|  3 | Amit     |   22 |
+----+----------+------+
3 rows in set (0.00 sec)

mysql> UPDATE student SET age = 23 WHERE id = 1;
Query OK, 1 row affected (0.05 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM student;
+----+----------+------+
| id | name     | age  |
+----+----------+------+
|  1 | Abir     |   23 |
|  2 | Manikant |   21 |
|  3 | Amit     |   22 |
+----+----------+------+
3 rows in set (0.00 sec)

mysql> UPDATE student SET age = age + 1;
Query OK, 3 rows affected (0.04 sec)
Rows matched: 3  Changed: 3  Warnings: 0

mysql> SELECT * FROM student;
+----+----------+------+
| id | name     | age  |
+----+----------+------+
|  1 | Abir     |   24 |
|  2 | Manikant |   22 |
|  3 | Amit     |   23 |
+----+----------+------+
3 rows in set (0.00 sec)

mysql>
mysql> UPDATE student SET age = age - 2;
Query OK, 3 rows affected (0.04 sec)
Rows matched: 3  Changed: 3  Warnings: 0

mysql> SELECT * FROM student;
+----+----------+------+
| id | name     | age  |
+----+----------+------+
|  1 | Abir     |   22 |
|  2 | Manikant |   20 |
|  3 | Amit     |   21 |
+----+----------+------+
3 rows in set (0.00 sec)

mysql> ALTER TABLE student ADD email VARCHAR(100);
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM student;
+----+----------+------+-------+
| id | name     | age  | email |
+----+----------+------+-------+
|  1 | Abir     |   22 | NULL  |
|  2 | Manikant |   20 | NULL  |
|  3 | Amit     |   21 | NULL  |
+----+----------+------+-------+
3 rows in set (0.00 sec)

mysql> DESC student;
+-------+--------------+------+-----+---------+-------+
| Field | Type         | Null | Key | Default | Extra |
+-------+--------------+------+-----+---------+-------+
| id    | int          | NO   | PRI | NULL    |       |
| name  | varchar(50)  | YES  |     | NULL    |       |
| age   | int          | YES  |     | NULL    |       |
| email | varchar(100) | YES  |     | NULL    |       |
+-------+--------------+------+-----+---------+-------+
4 rows in set (0.04 sec)

mysql> ALTER TABLE student DROP email;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC student;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | NO   | PRI | NULL    |       |
| name  | varchar(50) | YES  |     | NULL    |       |
| age   | int         | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> ALTER TABLE student CHANGE name full_name VARCHAR(50);
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC student;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| id        | int         | NO   | PRI | NULL    |       |
| full_name | varchar(50) | YES  |     | NULL    |       |
| age       | int         | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> SELECT COUNT(*) FROM student;
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+
1 row in set (0.05 sec)

mysql> SELECT MAX(age), MIN(age), AVG(age) FROM student;
+----------+----------+----------+
| MAX(age) | MIN(age) | AVG(age) |
+----------+----------+----------+
|       22 |       20 |  21.0000 |
+----------+----------+----------+
1 row in set (0.04 sec)

mysql>
