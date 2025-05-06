#Inheritance, polymorphism,encaspulation

#1. Inheritance->allows classes to inherit properties and methods from other classes.It helps reduce code repetition and create a natural hierarchy
class Vehicle:
  def __init__(self,wheels):
    self.wheels = wheels

class Car(Vehicle):
  pass

car = Car(4)
print(car.wheels)

#Polymorphism->allows methods to do different things based on the object it is acting upon, even if they share the same name.
class Dog:
  def speak(self):
    return "Woof!"

class Cat:
  def speak(self):
    return "Meow!"

#Polymorphism in action
for animal in[Dog(),Cat()]:
  print(animal.speak())



#Encaspulation-> This is the practice of keeping attributes and methods private to prevent unwanted interference from outside the class. It’s like hiding your chocolate stash 🍫 from everyone else!
class SecretStash:
  def __init__(self):
    self.__chocolate = 8 #private attribute

  def get_chocolate(self):
    return self.__chocolate #accessing private attribute through a public method
  
  def take_chocolate(self):
    if self.__chocolate > 0:
      self.__chocolate -= 1
      return "Yum!"
    else:
      return "No more chocolate left!"
    
stash = SecretStash()
print(stash.get_chocolate()) #accessing private attribute through a public method
print(stash.take_chocolate()) #accessing private method through a public method