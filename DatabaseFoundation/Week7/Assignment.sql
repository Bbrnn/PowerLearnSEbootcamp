-- Question 1 Achieving 1NF (First Normal Form) 🛠️
-- Task:You are given the following table ProductDetail:
-- OrderID	CustomerName	Products
-- 101	John Doe	Laptop, Mouse
-- 102	Jane Smith	Tablet, Keyboard, Mouse
-- 103	Emily Clark	Phone
-- In the table above, the Products column contains multiple values, which violates 1NF.
-- Write an SQL query to transform this table into 1NF, ensuring that each row represents a single product for an order

CREATE TABLE orders (
  orderID INT PRIMARY KEY, 
  customerName VARCHAR(50)
  );

CREATE TABLE productDetail (
  orderID INT,
  products VARCHAR(50),
  FOREIGN KEY (orderID) REFERENCES orders(orderID)
);


-- Question 2 Achieving 2NF (Second Normal Form) 🧩
-- You are given the following table OrderDetails, which is already in 1NF but still contains partial dependencies:
-- OrderID	CustomerName	Product	Quantity
-- 101	John Doe	Laptop	2
-- 101	John Doe	Mouse	1
-- 102	Jane Smith	Tablet	3
-- 102	Jane Smith	Keyboard	1
-- 102	Jane Smith	Mouse	2
-- 103	Emily Clark	Phone	1
-- In the table above, the CustomerName column depends on OrderID (a -- partial dependency), which violates 2NF.

-- Write an SQL query to transform this table into 2NF by removing partial dependencies. Ensure that each non-key column fully depends on the entire primary key.

CREATE TABLE orders (
  orderID INT PRIMARY KEY, 
  customerName VARCHAR(50)
  );

CREATE TABLE orderDetails (
  orderID INT,
  product VARCHAR(50),
  quantity INT,
  FOREIGN KEY (orderID) REFERENCES orders(orderID)
  );

-- Question 3 Achieving 3NF (Third Normal Form) 
-- You are given the following table CustomerOrders, which is already in 2NF but contains transitive dependencies:
-- OrderID	CustomerName	Country	TotalAmount
-- 101	John Doe	USA	500
-- 102	Jane Smith	Canada	300
-- 103	Emily Clark	USA	700
-- In the table above, the Country column depends on Customer
-- Name, which is a transitive dependency, violating 3NF.
-- Write an SQL query to transform this table into 3NF by removing transitive dependencies. Ensure that all non-key columns depend only on the primary key. 
CREATE TABLE customers (
  customerID INT PRIMARY KEY, 
  customerName VARCHAR(50),
  country VARCHAR(50)
  );
CREATE TABLE orders (
  orderID INT PRIMARY KEY, 
  customerID INT,
  totalAmount DECIMAL(10, 2),
  FOREIGN KEY (customerID) REFERENCES customers(customerID)
  );

