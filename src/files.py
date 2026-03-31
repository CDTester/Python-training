import os
# File handling
# open() has a few methods,
# r=Read (default), a=Append, w=Write, x=Create
# file handling:
# t=Text (default), b=binary 

file1 = "../test_data/data1.txt"

read_text1 = open(file1) # r=read, t=Text by default
print("\n.read()")
print(read_text1.read())
read_text1.close()

read_text2 = open(file1, "rt") # r=read, t=Text
print("\nfor loop")
for x in read_text2:
  print(x)
read_text2.close()

print("\nwith open() as f:")
with open(file1) as f:
  print(f.read())
  print(f.read(2))
# do no need close() when using with

print("\nread 2 characters from file:")
with open(file1) as f:
  print(f.read(2))

print("\nread 1 line from file:")
with open(file1) as f:
  print(f.readline())


print("\nappend 1 line to file:")
with open(file1, "a") as f:
  f.write("\nappend new line")
with open(file1) as f:
  print(f.read())

print("\nwrite will overwrite lines in file:")
with open(file1, "w") as f:
  f.write("line1\nline2\nline3")
with open(file1) as f:
  print(f.read())

print("\ncreate new file:")
with open("../test_data/file2.txt", "x") as f:
  f.write("line1\nline2\nline3")
with open(file1) as f:
  print(f.read())

print("\ndelete new file using os.remove:")
if os.path.exists("../test_data/file2.txt"):
  print("Removing file: ../test_data/file2.txt")
  os.remove("../test_data/file2.txt")
else:
  print("file ../test_data/file2.txt does not exist")