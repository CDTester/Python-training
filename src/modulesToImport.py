numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def my_function():
  print("Hello from my_function")

def f_to_c(farenheit):
  celsius = (farenheit - 32) * 5 / 9
  return celsius

def hello(name = "stranger"):
  print("Hello,", name)

# kwargs - keyword args, args can be sent in any order
def my_pet(animal, name):
  print("My", animal + "'s name is", name)

def no_kwargs(animal, name, /):
  print("My", animal + "'s name is", name)

def no_pos(*, animal, name,):
  print("My", animal + "'s name is", name)

# returning other data types
def get_fruits():
  return ["apple", "banana", "cherry"]

def coords():
  return (10, 20)