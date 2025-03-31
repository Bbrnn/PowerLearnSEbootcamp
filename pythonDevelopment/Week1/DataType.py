num1 = 55
num2 = 5.3
print(num1)
print(type(num1))
print(num2)
print(type(num2))

#List data type
#A list is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ].
languages = ["Python", "Dart", "Web", 23]
print(languages)
#access items in the list
print(languages[1])

#tuple data type
#A tuple is an ordered sequence of items same as a list. 
# The only difference is that tuples are immutable. In Python, we use the parentheses () to store items of a tuple.
products = ('Xbox', 588.32, "Habibi", 23)
print(products)
print(type(products))
#accessing items in a tuple
print(products[3])

#string data type
#String is a sequence of characters represented by either single or double quotes
site_name = "Power learn Project"
print(site_name)
print(type(site_name))

#set data type
#The Set is an unordered collection of unique items. Set is defined by values separated by commas inside braces { }
student_ids = {112, 114, 117, 113}
print(student_ids)
print(type(student_ids))
 #Note: Since sets are unordered collections, indexing has no meaning. Hence, the slicing operator [] does not work

 #dictionary data type
 #Python dictionary is an ordered collection of items. It stores elements in key/value pairs.
capital_city = {"Kenya":"Nair","Nigeria":"Lagos"}
print(capital_city)
print(type(capital_city))
