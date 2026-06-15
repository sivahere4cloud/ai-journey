show DATABASES;
USE sivadb;

SHOW TABLES;
USE SIVADB;
SHOW TABLES;
#DDL Commands = Data definition language
#Create,alter,drop
#DML Commands = Data Manipulation language
#insert,update,delete
# DCL Commands = Data Control Language
#Grant(gives privilege to user),Revoke(Takes back privilages granted from user)
#DQL Commands = Data Query Language
#Select
#Relational Database Management System(RDBMS)

#SQL Constraints: 
#Following are commonly used constraints available in SQL: 

#NOT NULL Constraint: Ensures that a column cannot have NULL value. 
#DEFAULT Constraint: Provides a default value for a column when none is specified. 
#UNIQUE Constraint: Ensures that all values in a column are different. 
#PRIMARY Key: Uniquely identified each rows/records in a database table. 
#FOREIGN Key: Uniquely identified a rows/records in any another database table. 
#CHECK Constraint: The CHECK constraint ensures that all values in a column satisfy certain conditions. 
#INDEX: Use to create and retrieve data from the database very quickly.
USE SIVADB;
CREATE TABLE CUSTOMERS( 
ID   INT              NOT NULL, 
NAME VARCHAR (20)     NOT NULL, 
AGE  INT              NOT NULL, 
ADDRESS  CHAR (25) , 
SALARY   DECIMAL (18, 2),        
PRIMARY KEY (ID) 
); 

ALTER TABLE CUSTOMERS MODIFY SALARY DECIMAL(18,2) NOT NULL;
ALTER TABLE CUSTOMERS MODIFY SALARY DECIMAL(18,2) DEFAULT 5000.00;
ALTER TABLE CUSTOMERS ALTER COLUMN SALARY DROP DEFAULT;

ALTER TABLE CUSTOMERS MODIFY AGE INT NOT NULL UNIQUE;

CREATE TABLE ORDERS(

    ID INT NOT NULL,
    DATE DATETIME,
    CUSTOMER_ID INT REFERENCES CUSTOMERS(ID),
    AMOUNT DOUBLE,
    PRIMARY KEY (ID)
    );

SELECT NOW();

/*DATA TYPE 

Bigint -9,223,372,036,854,775,808  TO 9,223,372,036,854,775,807 
Int -2,147,483,648  TO 2,147,483,647 
Smallint -32,768  TO 32,767 
Tinyint  0 TO 255 
Bit 0  TO 1 
Decimal -10^38 +1 TO 10^38 -1 
Numeric -10^38 +1  TO 10^38 -1 
Money -922,337,203,685,477.5808  TO +922,337,203,685,477.5807 
Smallmoney -214,748.3648  TO +214,748.3647 
*/


/*Date and Time Data Types: 

Datetime Jan 1, 1753 TO Dec 31, 9999 
Smalldatetime Jan 1, 1900 TO Jun 6, 2079 
Date Stores a date like June 30, 1991 
Time Stores a time of day like 12:30 P.M.

*/

/*Character Strings Data Types: DATA TYPE FROM TO 
Char Maximum length of 8,000 characters.( Fixed length non-Unicode 
characters) 
Varchar  Maximum of 8,000 characters.(Variable-length non-Unicode data). 
varchar(max) Maximum length of 231characters, Variable-length non-Unicode data 

Text text Variable-length non-Unicode data with a maximum length of 
2,147,483,647 characters.
*/

/*Unicode Character Strings Data Types: 

DATA TYPE Description 
Nchar Maximum length of 4,000 characters.
Nvarchar Maximum length of 4,000 characters.
nvarchar(max) Maximum length of 231characters 
Ntext Maximum length of 1,073,741,823 characters. 
*/
/*
Binary Data Types

DATA TYPE Description 
Binary Maximum length of 8,000 bytes
Varbinary Maximum length of 8,000 bytes.
varbinary(max) Maximum length of 231 bytes 
Image Maximum length of 2,147,483,647 bytes. 
*/
/*
Misc Data Types: 
 
sql_variant  Stores values of various SQL Server-supported data types, except text, ntext, and 
timestamp.   Stores a database-wide unique number that gets updated every time a row gets 
updated 
uniqueidentifier  Stores a globally unique identifier (GUID) 
xml  Stores XML data. You can store xml instances in a column or a variable 
cursor  Reference to a cursor object 
table  Stores a result set for later processing
*/

SELECT 10+20;
SELECT 10*20;
USE SIVADB;
INSERT INTO CUSTOMERS
(ID, NAME, AGE, ADDRESS, SALARY)
VALUES
(1, 'Ramesh', 32, 'Ahmedabad', 2000.00),
(2, 'Khilan', 25, 'Delhi', 1500.00),
(3, 'Kaushik', 23, 'Kota', 2000.00),
(4, 'Chaitali', 21, 'Mumbai', 6500.00),
(5, 'Hardik', 27, 'Bhopal', 8500.00),
(6, 'Komal', 22, 'MP', 4500.00),
(7, 'Muffy', 24, 'Indore', 10000.00);

SELECT * FROM CUSTOMERS WHERE SALARY >5000;

SELECT * FROM CUSTOMERS WHERE SALARY = 2000;
SELECT * FROM CUSTOMERS WHERE SALARY != 2000; 
SELECT * FROM CUSTOMERS WHERE SALARY >= 6500;
SELECT * FROM CUSTOMERS WHERE AGE >= 25 AND SALARY >= 6500;
 SELECT * FROM CUSTOMERS WHERE AGE IS NOT NULL;
 SELECT * FROM CUSTOMERS WHERE NAME LIKE 'Ko%';
 SELECT * FROM CUSTOMERS WHERE AGE IN ( 25, 27 );
 SELECT * FROM CUSTOMERS WHERE AGE BETWEEN 25 AND 27; 
 SELECT AGE FROM CUSTOMERS  
WHERE EXISTS (SELECT AGE FROM CUSTOMERS WHERE SALARY > 6500);     
SELECT * FROM CUSTOMERS  
WHERE AGE > ALL (SELECT AGE FROM CUSTOMERS WHERE SALARY > 6500); 
SELECT * FROM CUSTOMERS  
WHERE AGE > ANY (SELECT AGE FROM CUSTOMERS WHERE SALARY > 6500);

CREATE DATABASE DatabaseName; 
 CREATE DATABASE testDB; 

  SHOW DATABASES; 

DROP DATABASE DatabaseName; 
SHOW DATABASES;
USE SIVADB

 CREATE TABLE SALARY AS 
   SELECT ID, SALARY 
   FROM CUSTOMERS; 

SELECT * FROM SALARY;

DESC CUSTOMERS; 
 DROP TABLE ORDERS;

  DROP TABLE CUSTOMERS;

INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (1, 'Ramesh', 32, 'Ahmedabad', 2000.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (2, 'Khilan', 25, 'Delhi', 1500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (3, 'kaushik', 23, 'Kota', 2000.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (4, 'Chaitali', 25, 'Mumbai', 6500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY) 
VALUES (5, 'Hardik', 27, 'Bhopal', 8500.00 ); 
INSERT INTO CUSTOMERS (ID,NAME,AGE,ADDRESS,SALARY)

SELECT * FROM ORDERS;

UPDATE CUSTOMERS 
| ID | NAME     
SET ADDRESS = 'Pune', SALARY = 1000.00; 


DELETE FROM CUSTOMERS 
WHERE ID = 6; 
#SQL LIKE Clause
/*
SELECT FROM table_name 
WHERE column LIKE 'XXXX%' 
or  
SELECT FROM table_name 
WHERE column LIKE '%XXXX%' 
or 
SELECT FROM table_name 
WHERE column LIKE 'XXXX_' 
or 
SELECT FROM table_name 
WHERE column LIKE '_XXXX' 
or 
SELECT FROM table_name 
WHERE column LIKE '_XXXX_'*/

 SELECT * FROM CUSTOMERS 
WHERE SALARY LIKE '200%'; 


 SELECT TOP 3 * FROM CUSTOMERS; 

 SELECT * FROM CUSTOMERS 
LIMIT 3;

 SELECT * FROM CUSTOMERS 
ORDER BY NAME, SALARY; 


 SELECT * FROM CUSTOMERS 
ORDER BY NAME DESC; 

SELECT NAME, SUM(SALARY) FROM CUSTOMERS 
GROUP BY NAME;
# GROUP BY clause is used in collaboration with the SELECT statement to arrange identical data 

 SELECT SALARY FROM CUSTOMERS 
ORDER BY SALARY; 
# DISTINCT keyword is used in conjunction with SELECT statement to eliminate all the duplicate

SELECT * FROM CUSTOMERS 
     ORDER BY NAME DESC;




