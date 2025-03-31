"""
Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
"""
def Calculator(num1, num2):

  #Addition operation
  num_add = str(num1 + num2)
  num_subtract = str(num1 - num2)
  num_multiply = str(num1 * num2)
  num_divide = str(num1 / num2)
  print( "Result of addition is:", num_add)
  print( "Result of subtraction is:", num_subtract)
  print( "Result of multiplication is:", num_multiply)
  print( "Result of division is:", num_divide)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(Calculator(num1, num2))