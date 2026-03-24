# FOR LOOP 
print("FOR LOOPS")
# THROUGH STRINGS
print("through a string (array) using 'for x in \"banana\":'")
for x in "banana":
  print(x, end=", ")

# THROUGH LISTS
thislist = ["apple", "banana", "cherry"]
print("\n\nthislist =", thislist)
print("through a list (array) using 'for x in thislist:'")
for x in thislist:
  print(x, end=", ")

print("\nthrough a list (array) using 'for i in range(len(thislist)):'")
for i in range(len(thislist)):
  print(thislist[i], end=", ")

print("\nthrough a list comprehension using '[print(x) for x in thislist]'")
[print(x) for x in thislist]


print("\nthrough a dict keys using 'for x in thisdict:'")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "colors": ["red", "white", "blue"],
  "year": 1964,
  "year": 2026
}
for x in thisdict:
  print(x)

print("or through a dict keys using 'for x in thisdict.keys():'")
for x in thisdict.keys():
  print(x)

print("\nthrough a dict values using 'for x in thisdict:'")
for x in thisdict:
  print(thisdict[x])

print("or through a dict values using 'for x in thisdict.vales():'")
for x in thisdict.values():
  print(x)

print("\nthrough nested dict")
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
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])

print("\nbreak when at banana in list [apple, banana, cherry] ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("\ncontinue when at banana in list [apple, banana, cherry] ")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


print("\nElse print something after for loop")
for x in range(6):
  if x == 3: continue
  print(x, end=", ")
else:
  print("Finally finished!")

print("\nElse does not print something after for loop if loop breaks")
for x in range(6):
  if x == 3: break
  print(x, end=", ")
else:
  print("Finally finished!")


# WHILE LOOP
print("\n\nWHILE LOOPS")
i = 1
print("while i < 6")
while i < 6:
  print("i =",i)
  i += 1

print("\nbreaking the loop of while i < 6")
i = 1
while i < 6:
  print("i =",i)
  if i == 3:
    print("breaking at 3")
    break
  i += 1

print("\ncontinuing the loop of while i < 6")
i = 0
while i < 6:
  i += 1
  if i == 3:
    print("continue after 3")
    continue
  print("i =",i)

print("\nelse i is greater or equal to 6")
i = 1
while i < 6:
  print("i =",i)
  i += 1
else:
  print(f"i = {i} which is no longer less than 6")



print("\nthrough a list (array) using 'while i < len(thislist):' where len(thislist) = ", len(thislist))
i = 0
print("i =", i)
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  print("i =", i)

