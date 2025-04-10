CREATE TABLE student (
    name VARCHAR(100),      -- Name with a maximum length of 100 characters
    age INT,                -- Age as an integer
    gender VARCHAR(10)      -- Gender with a maximum length of 10 characters
);


insert into student(name, age, gender)
values
('Alice', 20,'Female'),
('Bob',22,'Male'),
('Charlie',21,'Monbinary');
