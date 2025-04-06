string1 ="Python Programming"
string1 = 'Python Programming'

name = "Python"
print(name)
message = "I love Python"
print(message)

#Accessing strings characters
#indexing
greet = 'hello'
print(greet[1])
print(greet[-4])

#slicing
print(greet[1:4])

#Python strings are immutable
message = 'Hola Amigos'
#message[0] = 'H'
print(message)
#However w=can assign the variable name to a  new string
message = 'Hello friends'
print(message)

#Python multiline string
#use triple double quotes or triple single quotes
message = """
Never gonna give you up
Never gonna give you down
"""
print(message)

#Python string Operations
#1. Compare two strings
str1 = "Hello, World!"
str2 = "I love Python."
str3 = "Hello, World!"

print(str1 == str2)
print(str1 == str3)

#Join two or more strings
greet = "Hello, "
name = "Jack"

result = greet + name
print(result)

#Iterate through a string
greet = "hello"
for letter in greet:
  print(greet)

#Python string length
#Use len()  
print(len(greet))

#String membership test
print('a' in 'program')
print('at' not in 'battle')

#string methods

#Escape sequences in python
example="He said, \"What's there?\""
example='He said, What\'s there?"'
print(example)


#Python String Formatting
#f-strings
name = "Cathy"
country = "UK"
print(f'{name} is from {country}')
