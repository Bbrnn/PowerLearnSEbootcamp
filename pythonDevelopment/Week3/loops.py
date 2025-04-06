"""
There are 2 types of loops in Python:

for loop
while loop

"""
#In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length.
fruits = ["apple","banana","cherry"]
for fruit in fruits:
  print(f"I love {fruit}")
          
#For Loops: Using Range
for number in range(1,6):
  print(f"Number: {number}")


"""
While Loops

A while loop performs a set of instructions as long as a given condition is true.

"""

count = 1
while count <= 5:
  print(f"Count: {count}")
  count+=1

#Loop controls: Break and continue
for number in range(1,10):
  if number == 5:
    print("Breaking the loop at 5")
    break
  elif number % 2 == 0:
    print(f"Skiipping {number} because it is even")
    continue
  print(f"Processing number: {number}")


  #Nested loops
  for i in range(1, 4):
    for j in range(1,4):
      print(f"Outer loop: {i}, Inner loop:{j}")