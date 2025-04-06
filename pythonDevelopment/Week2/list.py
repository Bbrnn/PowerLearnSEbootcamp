numbers = [1,2,3]
print(numbers)

#empty list
my_list = []
#list with mixed data types
my_list = [1,"hello",3.4]

#Access python list elements
languages = ["Python", "Swift", "C++"]
print(languages[2])
#slicing
print(languages[1:3])
my_list = ['p','r','a','g','i']
print(my_list[2:5])
print(my_list[:])

#Adding elements in a python list
#use append()
numbers = [21,33,12,76]
print('Before append:', numbers)
#using append method
numbers.append(44)
print('After append:', numbers)

#Using extend- add all items of one list to another
prime_numbers = [2,3,5]
even_numbers = [4,6,8]
prime_numbers.extend(even_numbers)

print("List after extending:", prime_numbers)

#Changing list items
#Lists are mutable
languages = ["Python", "Swift", "C++"]
languages[2] = 'C'
print(languages)

#Remove an item from a list
#1. using del
languages = ["Python","Swift","C++","C","Java","Rust","R"]
del(languages[3])
print(languages)
del(languages[-1])
print(languages)
del languages[0:2]
print(languages)
#2. remove()-method to delete a list item
languages.remove('Rust')
print(languages)

#Iterating through a list
languages = ["Python", "Swift", "C++"]
for language in languages:
  print(language)


#Python list comprehension
#A list comprehension consists of an expression followed by the for statement inside square brackets.
numbers = [number * number for number in range(1,6)]
print(numbers)
