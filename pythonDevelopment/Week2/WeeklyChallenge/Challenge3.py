"""
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
"""
name= input("What is your name?")
age = input("What is your age?")
fav_color = input("What is your favorite color?")

person = {'Name':name,'Age':age,'Favorite color':fav_color}
print(person)