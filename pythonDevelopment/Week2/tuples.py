#Tuples is similar to a list but they are immutable to mean elements cannot be changed 
#In Python, creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.

var1 = ("hello")
print(type(var1))
var2 = ("hello",)
print(type(var2))
var3 = "hello",
print(type(var3))

#Accessing python tuple elements
#1.indexing
letters = ("p","q","r","s","t","o","z","x","m","l")
print(letters[0])
print(letters[6])

#2.Negative indexing
print(letters[-1])
print(letters[-3])


#Python Tuple Methods
my_tuple = ('a', 'p','m','o','w','q','w')
print(my_tuple.count('w'))
print(my_tuple.index('o'))