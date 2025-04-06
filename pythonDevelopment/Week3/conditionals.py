"""
In Python, there are three forms of the if...else statement.

if statement
if...else statement
if...elif...else statement
"""

#1.If statement
temp = 30
if temp > 25:
  print("It's a hot day!")

 # 2. If else statement

temp = 40
if temp > 45:
  print("It's a hot day!")
else:
  print("It's a cool day !")

#3.If ..elif ..else statement
temp = 15
if temp > 25:
  print("It's a hot day!")
elif temp >15:
  print("It's a warm day!")
else:
  print("It's a cold day!")