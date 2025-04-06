"""
Functions are a fundamental part of Python programming. They allow you to encapsulate reusable blocks of code to make programs modular, easier to understand, and maintain.
A function is a block of code designed to perform a specific task. 
"""

#Syntax
value= 3
def function_name(parameters):
    """Optional docstring explaining the function."""
    # Code block
    return value  # Optional return statement

    """
    

Types of Functions
Built-in Functions: Predefined functions in Python (e.g., print(), len(), type()).
User-defined Functions: Functions created by the user.
    """

def greet(name):
    return f"Hello,{name}"
print(greet("Alice"))

"""
Key Components of a Function
Function Name: Should be descriptive and follow naming conventions.
Parameters: Variables passed into the function.
Docstring: An optional description of what the function does.
Return Statement: Outputs a value from the function (optional).
"""
#Positional arguements
def add(a,b):
    return a + b
print(add(3,5))

#Default arguements

def greet(name="Guest"):
    return f"Hello, {name}"
print(greet())
print(greet("Alice"))

#Keyword arguements
def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob"))

#Returning values

def square(number):
    return number ** 2
result = square(4)
print(result)

#Anonymous functions: Lambdas

# Lambda function for adding two numbers
add = lambda x, y: x + y
print(add(3, 5))

# Using lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]
                  

#Recursive Functions

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))