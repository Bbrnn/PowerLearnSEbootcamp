"""
A list comprehension is a compact syntax for creating a list by evaluating an expression for each element in an iterable (like a list or range), optionally filtering elements based on a condition

Syntax:

[expression for item in iterable if condition]
expression: The value or transformation applied to each element.
item: A variable that represents each element in the iterable.
iterable: A sequence (like a list, tuple, or range) to iterate over.
condition: (Optional) A filter that determines whether to include the element.
"""

#Traditional loop
squares = []
for x in range(5):
  squares.append(x**2)
  #print(squares)

#list comprehension
squares1 = [x**2 for x in range(5)]
print(squares1)

#Using conditions in list comprehensions
even_numbers = [ x for x in range(10) if x % 2 == 0]
print(even_numbers)

#Nested List Comprehensions
#List comprehensions can be nested to handle complex operations, such as creating a matrix.
#Create a 3x3 matrix using nested list comprehensions

matrix = [[i * j for j in range(1,4)] for i in range(1,4)]
print(matrix)

#Examples of list comprehensions
#1.Transforming data
names = ["Alice","Bob","Charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)

#2.Filtering data
numbers = [10, 15, 20, 25, 30]
divisible_by_5 = [num for num in numbers if num % 5 == 0]
print(divisible_by_5)

#3. Flattening a List:
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

#When not to use list comprehensions- complex
# Complex list comprehension (less readable)
result = [x * y for x in range(10) for y in range(5) if x + y > 5]

# Better as a loop (more readable)
result = []
for x in range(10):
    for y in range(5):
        if x + y > 5:
            result.append(x * y)

print(result)