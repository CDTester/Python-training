class Person:
  x = 5
  species = "Human" # Class property

  def __init__(self, name, age): # doesn't have to be self, can be e.g. this
    self.name = name # Instance property
    self.age = age   # Instance property
    self.hobbies = []
    self.__sex = "" # __ makes the property private
    self._salary = 0 # _ makes the property protected, this is just naming convention, not enforced by Python

  def __str__(self):
    return f"{self.name} ({self.age})"
  
  def describe(self):
    if self.age < 2: year = "year"
    else: year = "years"
    print(f"{self.name} is {self.age} {year} old.")

  def lives(self):
    try:
      print(f"{self.name} lives in {self.city}")
    except:
      print("City has not yet been defined")

  def add_hobby(self, hobby):
    self.hobbies.append(hobby)
    print(f"Added: {hobby}")

  def remove_hobby(self, hobby):
    if hobby in self.hobbies:
      self.songs.remove(hobby)
      print(f"Removed: {hobby}")

  def show_hobbies(self):
    print(f"{self.name}'s hobbies:")
    for hobby in self.hobbies:
      print(f"- {hobby}")
  
  # Encapsulation
  def setSex(self, sex):
    self.__sex = sex

  # Encapsulation
  def getSex(self):
    print(f"{self.name} is a {self.__sex}")