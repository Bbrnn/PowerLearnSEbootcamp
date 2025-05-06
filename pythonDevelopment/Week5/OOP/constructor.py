class Car:
  #constructor->_init__ method allows each object to start with specific values
  def __init__(self, color, model):
    self.color = color
    self.model = model
  
#Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red"," SUV")

print(car1.color)
print(car2.model)