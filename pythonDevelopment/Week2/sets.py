#Set is a collection of unique data
#Elements of a set cannot be duplicated

student_id = {112,114,116,118,115}
print("Student ID:", student_id)
vowel_letters = {'a','e','i','o','u'}
print('Vowel letters:', vowel_letters)

#set of mixed data atypes
mixed_set = {"Hello", 101, -2, 'Bye'}
print("Set of mixed data types:", mixed_set)

#Create an empty set in python
#Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python
#To make a set without any elements, we use the set() function without any argument.

#create an empty set
empty_set = set()
#Create an empty dictionary
empty_dictionary = {}

print(type(empty_set))
print(type(empty_dictionary))

#Dulpicate items in a set
numbers = {2,4,6,6,2,8}
print(numbers)
#There are no duplicate items in a set
#Set cannot contain duplicates

#Add and uodate set items in python
#Sets are mutable. However, since they are unordered, indexing has no meaning.


#We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.


numbers = {21,34,54,12}
print("Initial set numbers", numbers)
numbers.add(32)
print("Updated Set:", numbers)


#Update Python set
#The update() method is used to update the set with items other collection types (lists, tuples, sets, etc).

companies = {'Lacoste','Ralph Lauren'}
tech_companies = ['apple','google','apple']

companies.update(tech_companies)
print(companies)

#Remove elements from a set
#We use the discard() method to remove the specified element from a set.
languages = {'Swift','Java','Python'}
print('Initial set:', languages)

removedValue = languages.discard('Java')

print('Set after remove():', languages)

#Iterate over a set

fruits = {'Apple','Peach',"Mango"}
for fruit in fruits:
  print(fruit)

#Number of set elements
even_numbers  = {2,4,6,8}
print('Set:',even_numbers)

print('Total elements:',len(even_numbers))

#Python set Operations

#1.Union of two sets
#The union of two sets A and B include all the elements of set A and B.
A ={1,3,5}
B = {0,2,4}
print('Union using |:', A | B)
print('Union using union():',A.union(B))

#Set intersection
#The intersection of two sets A and B include the common elements between set A and B.

A = {1,3,5}
B = {1,2,3}
print('Intersection using &:', A&B)
print()
print('Intersection using intersection():', A.intersection(B))


#Difference between Two Sets

#The difference between two sets A and B include elements of set A that are not present on set B.
#USE - OR difference()


#Set Symmetric Difference

#The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
#USE ^