from myPackage.Person import *
from myPackage.inheritance import *

p1 = Person("Andy", 1)
print(p1.x)
p1.describe()

del p1
try:
  print(p1.x)
except:
  print("p1 was deleted")

p2 = Person("Emil", 36)

p2.describe()
print(p2.name)
print(p2.age)
p2.age = 37
print(p2.age)

p2.lives()
p2.city = "London"
p2.lives()

print(p2) # calls the __str__ method

p2.add_hobby("Coding")
p2.add_hobby("Testing")
p2.show_hobbies()

s1 = Student("Mike", 50) # Student is a child class (inheritance) of Person
s1.describe()
s1.enrol("Physics")
s1.studying()

try:
  print("Emil's sex is ", s1.__sex)
except:
  print("Error: __sex cannot be accessed outside of the Person class")
s1.setSex("male")
s1.getSex()
s1._salary = 25000
print(s1._salary)
