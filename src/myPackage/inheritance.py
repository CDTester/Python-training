from myPackage.Person import *

class Student(Person):
  def __init__(self, name, age):
    super().__init__(name, age) # if you have __init__ in the shild class, you can add the __init__ from the parent
  
  def enrol(self, course):
    self.course = course
    print(f"{self.name} has been enrolled on to the {self.course} course.")
  
  def studying(self):
    try:
      print(f"{self.name} is studying {self.course}")
    except:
      print(f"{self.name} is not currently studying anything")

  # polymorphism, describe exists on Person
  def describe(self):
    super().describe()
    self.studying()