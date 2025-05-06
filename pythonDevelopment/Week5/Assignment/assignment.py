class Person:
  def __init__(self, name, age, occupation):
    self.name = name
    self.age = age
    self.occupation = occupation  
  
  def display_info(self):
    return f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}"

  def work(self):
    return f"{self.name} is working as a {self.occupation}."

#inheritance
class Student(Person):
  def __init__(self, name, age, occupation, major):
    super().__init__(name, age, occupation)
    self.major = major

  def study(self):
    return f"{self.name} is studying {self.major}."

#example
person = Person("John Doe", 30, "Software Engineer")
student = Student("Jane Doe", 20, "Student", "Computer Science")
print(person.display_info())
print(person.work())
print(student.display_info())
print(student.work())
print(student.study())


#polymorphism 
class PersonPolymorphism:
  def role(self):
    pass

class Teacher(PersonPolymorphism):
  def role(self):
    return "Teaching students"

class Doctor(PersonPolymorphism):
  def role(self):
    return "Treating patients"

class Engineer(PersonPolymorphism):
  def role(self):
    return "Designing and building structures"

#example usage
if __name__ == "__main__":
  teacher = Teacher()
  doctor = Doctor()
  engineer = Engineer()

  for person in (teacher, doctor, engineer):
    print(person.role())
  
#Output:
# Name: John Doe, Age: 30, Occupation: Software Engineer







  
