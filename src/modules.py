# sys module 
import sys
import platform
import random
import modulesToImport as fn
from modulesToImport import my_function
import date

print("\nMODULES:")

print(sys.version)
print(sys.version_info)
print(platform.system())
print("random between 1 and 10:", random.randrange(1,10))
print("32 farenheit =", fn.f_to_c(32), "celsius")
print("use variables from modules. numbers =", fn.numbers)
print("dir(fn) =",dir(fn))
my_function()

now = date.now()
print("now =", now)
print("Weekday from now = ", date.fmt(now, "%A"))