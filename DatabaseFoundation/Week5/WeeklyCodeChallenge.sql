--Write an SQL query to create a table called student with the following columns:
--name (String, maximum length of 100 characters)
--age (Integer)
--gender (String, maximum length of 10 characters)
--Write an SQL query to create an index named IdxAge from Student table.

CREATE TABLE student (
  name VARCHAR(100),
  age INT,
  gender VARCHAR(10)
);

-- Insert sample data
INSERT INTO student (name, age, gender) VALUES
('Alice', 20, 'Female'),
('Bob', 22, 'Male'),
('Charlie', 19, 'Male'),
('Diana', 21, 'Female');


-- Create an index named IdxAge from Student table
CREATE INDEX IdxAge ON student (age);

SELECT * FROM student;