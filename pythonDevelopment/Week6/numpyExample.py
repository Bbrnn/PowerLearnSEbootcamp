import numpy as np

#Create a simple array

my_array = np.array([1,2,3,4,5])
print("Array:",my_array)

#perform operations
print("Array * 2", my_array * 2)
print("Mean:",np.mean(my_array))
#Create an array with numbers 10 to 50.
array1 = np.arange(10,51)
print("Array 10 to 50:",array1)
#Find the maximum and minimum values.
print("Max:",np.max(array1))
print("Min:",np.min(array1))

#Multiply all elements by 3.
print("Array1 * 3", array1 * 3)