print("\nTRY, EXCEPT, ELSE")

try:
  print(x)
except NameError:
  print("Variable x is not defined")

print("\nYou can have many exceptions, so you can have different messages for that suit the exception")
x = {"name": "Andy"}
try:
  print(x["age"])
except KeyError:
  print("key is not defined")
except NameError:
  print("Variable x is not defined")

print("\nElse is used if no errors occured")
try:
  print(x["name"])
except KeyError:
  print("key is not defined")
else:
  print("Nothing went wrong")

print("\nFinally is used if errors does or does not occur")
try:
  print(x["names"])
except KeyError:
  print("key is not defined")
finally:
  print("Finally end gracefully")

print("Raise - you can raise an exception if a condition is not met.")
a = -1
if a < 0:
  raise Exception("Sorry, no numbers below zero")
