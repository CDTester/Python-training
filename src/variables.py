"""
Python does not have a command to declare variables
"""

# int
x = 5

# string
y = "Hello World!"

print(x, ": is an integer") # string can be in either ""
print(y + ': is a string')  # or '' NB: + in print concatenates strings
print(2 + 5, "Adds 2 + 5")  # but with numbers the + adds the numbers 

# CASE SENSITIVE
print("\nCASE SENSITIVE: Variables are case sensitive")
a = 4
A = "Chris"
print("a =", a)
print("A =", A)

# CASTING
print("\nCASTING: specifying data type of a variable") 
b = str(3)
c = int(3)
d = float(3)

print(b, type(b))
print(c, type(c))
print(d, type(d))

# VARIABLE NAMES
print("\nVARIABLE NAMES: variables dont have to be single value strings")
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords:
and, as, assert, async, await, break, case, class, continue, def, del, elif, else, except, False, finally,
for, from, global, if, import, in, is, lambda, match, None, nonlocal, not, or, pass, raise, return, True, 
try, while, with, yield
"""
myvar = "myvar"
my_var = "my_var"
_my_var = "_my_var"
myVar = "myVar"
MYVAR = "MYVAR"
myvar2 = "myvar2"
# illegal names
# 2myvar = "John"
# my-var = "John"
# my var = "John"
print(myvar,my_var, _my_var, myVar, MYVAR, myvar2, sep=", ")

# ASSIGN MULTI VALUES
print("\nASSIGN MULTI VARIABLES")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# COLLECTION
print("\nCOLLECTION: UNPACKING")
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
x, y, z = fruits
print(x)
print(y)
print(z)

# GLOBAL VARIABLES
print("\nGLOBAL VARIABLES")
x = "awesome"
awe = "awesome"
y = "global var"

def myfunc():
  print("Python is " + x)
  y = "local var"
  print(y)
  global z
  z = "new global var created inside a function"
  global awe
  awe = "override global variable from inside function"

myfunc()
print(z)
print(awe)

# DATA TYPES
print("\nDATA TYPES")
"""
Python has the following data types built-in by default, in these categories:
  * Text Type:	    str
  * Numeric Types:	int, float, complex
  * Sequence Types:	list, tuple, range
  * Mapping Type:	  dict
  * Set Types:	    set, frozenset
  * Boolean Type:	  bool
  * Binary Types:	  bytes, bytearray, memoryview
  * None Type:	    NoneType
"""
x = "hello" # ---- or str("hello")
print(x, type(x))
x = 20 # --------- or int(20)
print(x, type(x))
x = 20.5 # ------- or float(20.5)
print(x, type(x))
x = 1j # --------- or complex(1j)
print(x, type(x))
x = ["hello","world" ,"!"]  # or list(("apple", "banana", "cherry"))
print(x, type(x))
x = ("hello","world" ,"!")  # or tuple(("apple", "banana", "cherry"))
print(x, type(x))
x = range(6)
print(x, type(x))
x = {"key1":"value","key2":"value"} # or dict(name="John", age=36)
print(x, type(x))
x = {"hello","world" ,"!"} # -------- or set(("apple", "banana", "cherry"))
print(x, type(x))
x = frozenset({"apple", "banana", "cherry"}) 
print(x, type(x))
x = True # -------- or bool(5) 
print(x, type(x))
x = b"Hello" # ---- or bytes(5)
print(x, type(x))
x = bytearray(5)
print(x, type(x))
x = memoryview(bytes(5))
print(x, type(x))
x = None
print(x, type(x))

print("\nDATA TYPE: Numbers")
f1 = -35.59
f2 = 35e3
f3 = -87.7e100
print("Floats:", f1, "(-35.59)", f2, "(35e3)", f3, "(-87.7e100)")
c1 = 3+5j
c2 = 5j
c3 = -5j
# Complex numbers are written with a "j" as the imaginary part
print("complex:", c1, "(3+5j)", c2, "(5j)", c3, "(-5j)")


print("\nDATA TYPE: Strings")
s1 = """Use triple quotes
(single or double)
when you want 
multiline strings"""
print(s1)

s2 = "String is an Array"
print("s2 =", s2)
print("s2[1]: position 1 in array =", s2[1])
print("s2[:6]: Slicing the string from position 0 to  6 =", s2[0:6]) # note position 6 does not get included
print("s2[2:6]: Slicing the string from position 2 to  6 =", s2[2:6]) # note position 6 does not get included
print("s2[-5:-1]: Slicing the string from the last position to the 5th from last =", s2[-5:-1]) # note position 6 does not get included
print("len(s2): This gives us the length of the string =", len(s2))
print("\"an\" in s2: Checks if 'an' is in the string", "an" in s2)
print("\"integer\" not in s2: Checks if 'integer' is NOT in the string", "integer" not in s2)
print("s2.upper(): returns the string in uppercase =", s2.upper())
print("s2.lower(): returns the string in lowercase =", s2.lower())
print("s2.strip(): removes whitespace at beginning and end of string =", s2.strip())
print("s2.replace(\" \",\"_\"): replaces the first value with the second value =", s2.replace(" ", "_"))
print("s2.split(\" \"): splits the string into a list based on a splitter value =", s2.split(" "))

s3 = "Hello"
s4 = "World"
print("s3 =", s3)
print("s4 =", s4)
print("s3 + s4: concatenates the strings =", s3 + s4)

age = 36
txt = "My name is John, I am "
ftxt = f"{txt} {age}"
print("age =", age)
print("txt =", txt)
print("F-Strings (formatting string): f\"{txt} {age}\" =", ftxt)
txt = txt1 = "My name is {fname}, I'm {age}"
print("txt =", txt)
print("txt.format(fname=\"Sam\", age=36):  =", txt.format(fname="Sam", age=36))


price = 36
txt = "The price is {price:.2f} dollars"
ftxt = f"The price is {price:.2f} dollars"
print("price =", price)
print("txt =", txt)
print("Modified F-Strings: Change the type in f-string using {price:.2f} =", ftxt)


print("\nDATA TYPE: Booleans")
print("10 > 9:", 10 > 9)
print("10 == 9:", 10 == 9)
print("10 < 9:", 10 < 9)

print("\nDATA TYPE: Collections (arrays) ")
print("List       - is ordered,   changeable,   Allows duplicate members.")
print("Tuple      - is ordered,   unchangeable, Allows duplicate members.")
print("Set        - is unordered, unchangeable, and unindexed, No duplicate members.")
print("Dictionary - is ordered,   changeable,   No duplicate members.")
print("Negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.")

print("\nDATA TYPE: Lists ")
# Lists are used to store multiple items in a single variable. 
# List items are ordered, changeable, and allow duplicate values.
difTypesList = ["abc", 34, True, 40, "male"]
print("lists can contain multiple types, difTypesList =", difTypesList)
thislist = ["apple", "banana", "cherry"]
print("thislist =", thislist)
print("len(thislist):", len(thislist))
print("negative Indexing, thislist[-1]:", thislist[-1])
print("range Indexing, thislist[1:3]:", thislist[1:3])
thislist[0] = "berry"
print("Change item value, thislist[0] = \"berry\":", thislist)
thislist[1:3] = ["orange", "kiwi"]
print("Change range of item values, thislist[1:3] = [\"orange\", \"kiwi\"]:", thislist)
thislist[1:2] = ["grape", "plum"]
print("inserting more items than the range, thislist[1:2] = [\"grape\", \"plum\"]:", thislist)
thislist.insert(2, "date")
print("thislist.insert(2, \"date\"):", thislist)
thislist.append("berry")
print("thislist.append(\"berry\"):", thislist)
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("tropical =", tropical)
print("thislist.extend(tropical), thislist:", thislist)
thislist.remove("berry")
print("thislist.remove(berry), thislist:", thislist)
thislist.pop()
print("thislist.pop(), thislist:", thislist)
thislist.pop(1)
print("thislist.pop(1), thislist:", thislist)
del thislist[0]
print("del thislist.[0], thislist:", thislist)
thislist.clear()
print("thislist.clear(), thislist:", thislist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print("thislist =", thislist)
thislist.sort()
print("thislist.sort():", thislist)
thislist = [100, 50, 65, 82, 23]
print("thislist =", thislist)
thislist.sort(reverse=True)
print("thislist.sort(reverse=True):", thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("thislist =", thislist)
thislist.sort()
print("thislist.sort(): ",thislist)
thislist.sort(key = str.lower)
print("thislist.sort(key = str.lower): ",thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print("thislist =", thislist)
thislist.reverse()
print("thislist.reverse():", thislist)
mylist = thislist.copy()
print("mylist = thislist.copy():", mylist)
myotherlist = list(thislist)
print("myotherlist = list(thislist):", myotherlist)

print("\nList comprehension enables you to create a new list based on the values of an existing list.")
print("E.g. Based on a list of fruits, you want a new list with only fruits with the letter 'a' in the name.")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print("fruits = ", fruits)
print("[x for x in fruits if \"a\" in x]")
newlist = [x for x in fruits if "a" in x]
print("newlist =", newlist)

print("\nDATA TYPE: Tuples ")
# Tuples are used to store multiple items in a single variable. 
# A tuple is a collection which is ordered and unchangeable.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
thistuple = ("apple", "banana", "cherry", "banana")
print("thistuple =", thistuple)
thattuple = tuple(("abc", 34, True, 40, "male"))
print("thattuple =", thattuple)
print("The only way to add to a tuple (without converting to a list) is to add it to another tuple")
thistuple += thattuple
print("thistuple += thattuple =", thistuple )

print("\nDATA TYPE: Sets ")
# Sets are used to store multiple items in a single variable. 
# A set is a collection which is unordered, unchangeable (but you can add and remove items), and unindexed.
thisset = {"apple", "banana", "cherry"}
print("thisset stored as {\"apple\", \"banana\", \"cherry\"}")
print("thisset =", thisset)
thatset = {"apple", "banana", "cherry", "apple", "plum"}
print("thatset stored as {\"apple\", \"banana\", \"cherry\", \"apple\", \"plum\"}")
print("No duplicates allowed, thatset =", thatset)

print("You cannot access items in a set by referring to an index or a key. But you can loop through them.")
for x in thatset:
  print(x)

thisset.add("orange")
print("thisset.add(\"orange\") =", thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print("tropical =", tropical)
print("thisset.update(tropical) =", thisset)
mylist =  ["kiwi", "orange"]
thisset.update(mylist)
print("mylist =", mylist)
print("thisset.update(mylist) =", thisset)

thisset.remove("papaya") # removes will throw an error if item does not exist
print("\nthisset.remove(\"papaya\") =", thisset)
thisset.discard("pineapple") # discard is safer as it does not throw error if it does not exist
print("thisset.discard(\"pineapple\") =", thisset) 
popped = thisset.pop()
print("thisset.pop() will remove", popped)
print("thisset", thisset)

print("\nthisset.clear() will remove all items but keep thisset as set()")
print("del thisset will remove the set, calling thisset will throw an error")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = set1.union(set2, set3)
print("\nset1 =", set1)
print("set2 =", set2)
print("set3 =", set3)
print("set3 = set1.union(set2, set3) or set1 | set2 | set3 = ", set4) # | only lets you join sets, union allows other data types

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("\nset1 =", set1)
print("set2 =", set2)
set3 = set1.intersection(set2)
print("set3 = set1.intersection(set2) or set1 & set2 = ", set3) # & only lets you join sets, union allows other data types


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("\nset1 =", set1)
print("set2 =", set2)
set1.intersection_update(set2)
print("set1.intersection_update(set2) = ", set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("\nset1 =", set1)
print("set2 =", set2)
set3 = set1.difference(set2)
print("set3 = set1.difference(set2) or set1 - set2 = ", set3) # - only lets you join sets, union allows other data types

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("\nset1 =", set1)
print("set2 =", set2)
set1.difference_update(set2)
print("set1.difference_update(set2) = ", set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("\nset1 =", set1)
print("set2 =", set2)
set3 = set1.symmetric_difference(set2)
print("set3 = set1.symmetric_difference(set2) or set1 ^ set2 = ", set3) # ^ - only lets you join sets, union allows other data types

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("\nset1 =", set1)
print("set2 =", set2)
set1.symmetric_difference_update(set2)
print("set1.symmetric_difference_update(set2) = ", set1)

froze = frozenset({"apple", "banana", "cherry"})
print("froze =", froze)
print("Frozesets are immutable, they cannot be added to, removed or changed.")
print("However you can use union, difference, intersection and symmetric_difference")

print("\nDATA TYPE: Dictionaries")
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "colors": ["red", "white", "blue"],
  "year": 1964,
  "year": 2026
}
print("thisdict was created with year = 1964 and 2026. The later replaces the former.")
print("thisdict =", thisdict)
print("thisdict[\"brand\"] =", thisdict["brand"])
print("thisdict.get(\"model\") =", thisdict.get("model"))
print("len(thisdict) =", len(thisdict))
print("thisdict.keys() =", thisdict.keys())
print("thisdict.values() =", thisdict.values())
print("thisdict.items() =", thisdict.items())

thisdict["model"] = "focus"
print("\nthisdict[\"model\"] = \"focus\" =", thisdict)
thisdict["colors"].append("green")
print("thisdict[\"colors\"].append(\"green\") =", thisdict)
thisdict["country"] = "UK"
print("thisdict[\"country\"] = \"UK\" =", thisdict)
thisdict.update({"year": 2020})
print("thisdict.update({\"year\": 2020}) =", thisdict)
thisdict.pop("colors")
print("thisdict.pop(\"colors\") =", thisdict)
thisdict.popitem()
print("thisdict.popitem() #should remove country =", thisdict)
del thisdict["year"]
print("del thisdict[\"year\"] =", thisdict)

mydict = thisdict.copy()
print("mydict = thisdict.copy() =", mydict)

print("\nNested Dictionaries")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("myfamily =", myfamily)
print("myfamily[\"child2\"][\"name\"] =", myfamily["child2"]["name"])
