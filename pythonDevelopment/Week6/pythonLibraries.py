#A Python library is a collection of pre-written code that you can use to perform common tasks without having to write everything from scratch.

import math
print(math.sqrt(16))
print(math.pi)

from math import sqrt, pi

print("Square root of 36:", math.sqrt(36))

import random
print("Random numbe r between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice([1, 2, 3, 4, 5]))


import datetime
today = datetime.date.today()
print("Today's date is:", today)
