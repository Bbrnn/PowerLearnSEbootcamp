"""
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
"""
set1 = {'a','b','c','d'}
set2 = {'a','e','c','d','h'}
set3 = set1 & set2
print(set3)