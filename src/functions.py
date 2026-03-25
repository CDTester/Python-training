import sys
# FOR LOOP 
# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.

print("DEF - FUNCTIONS")
# basic function
def my_function():
  print("Hello from my_function")

def f_to_c(farenheit):
  celsius = (farenheit - 32) * 5 / 9
  return celsius

def hello(name = "stranger"):
  print("Hello,", name)

my_function()

# number args
print("77 farenheit =", f_to_c(77), "celsius")
print("32 farenheit =", f_to_c(32), "celsius")
print("0 farenheit =", f_to_c(0), "celsius")

# string args
hello("Chris")
hello() # will use default value in function

# kwargs - keyword args, args can be sent in any order
def my_pet(animal, name):
  print("My", animal + "'s name is", name)

def no_kwargs(animal, name, /):
  print("My", animal + "'s name is", name)

def no_pos(*, animal, name,):
  print("My", animal + "'s name is", name)

my_pet(name = "kwarg", animal = "dog")
my_pet("cat", "dave")
no_kwargs("fish", "nokwarg") # throws position-only argument error
no_pos(name = "nopos", animal = "parrot")  # does not allow positional args


# returning other data types
def get_fruits():
  return ["apple", "banana", "cherry"]

def coords():
  return (10, 20)

fruits = get_fruits()
print(fruits[1])
x, y = coords()  # return a tuple
print("x:", x,", y:", y) 


# Unknown amount of arg - arbitrary args
print("\nArbitrary args:")
def unknown_args(*kids):
  print("The youngest child is " + kids[2])

def max_num(*numbers):
  if len(numbers) == 0: return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num: max_num = num
  return max_num

def arb_kwargs(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

unknown_args("Emil", "Tobias", "Linus")
print("max num =", max_num(3,7,8,12,9,1,0,25))
arb_kwargs("emil123", age = 25, city = "Oslo", hobby = "coding", shoe_size = 9)

# DECORATORS
# A decorator is a function that takes another function as input and returns a new function.
print("\nDecorators:")
def decorator(up):
  def myinner(*args, **kwargs):
    return up(*args, **kwargs).upper()
  return myinner

def addgreeting(greet):
  def myinner(*args, **kwargs):
    return "Hello " + greet(*args, **kwargs) + " Have a good day!"
  return myinner

@decorator
@addgreeting
def decorated(name):
  return name

print(decorated("Steve"))

# LAMBDA - A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
print("\nLambda:")
x = lambda a, b : a * b
print(x(5, 6))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# RECURSION - Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
print("\nRecursion:")
def countdown(n):
  # Base case
  if n <= 0:
    print("Done!")
  # Recursive case
  else:
    print(n)
    countdown(n - 1)

countdown(5)

# The Fibonacci sequence is a series of numbers where each number (Fibonacci number)
# is the sum of the two preceding ones, usually starting from 0 and 1, or 1 and 1. 
# The sequence commonly begins 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

print("System recursion limit = ", sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("System recursion limit = ", sys.getrecursionlimit())


# GENERATORS - Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. 
# The function only executes when you iterate over the generator.
# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.
print("\nRecursion:")

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

print("You can manually iterate through a generator using the next() function:")
# This doesn't create a million numbers in memory
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))