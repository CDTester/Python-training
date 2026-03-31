print("\nOPERATORS: Arithmetic")
# Arithmetic operators are used with numeric values to perform common mathematical operations
x = 15
y = 4
print("x = ", x)
print("y = ", y)
print("x + y = ", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)
print("x ** y =", x ** y) 
print("x // y =", x // y) # return integer, rounded down

print("\nOPERATORS: Assignment")
# Assignment operators are used to assign values to variables:
x = 5
print("x = 5:", x)
x += 3
print("x += 3:", x)
x -= 2
print("x -= 2:", x)
x *= 100
print("x *= 100:", x)
x /= 10
print("x /= 10:", x)
x %= 50 
print("x %= 50:", x)
x //= 3
print("x //= 3:", x)
x **= 3
print("x **= 3:", x)
x = int(x)
x &= 3
print("x &= 3:", x)
x |= 3
print("x |= 3:", x)
x ^= 3
print("x ^= 3:", x)
x >>= 3
print("x >>= 3:", x)
x <<= 3
print("x <<= 3:", x)

# WALRUS OPERATOR
# The := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
# The count variable is assigned in the if statement, and given the value 5:
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

print("\nOPERATORS: Comparison")
# Comparison operators are used to compare two values:
x = 5
y = 3
print("x =", x)
print("y =", y)
print("x == y",x == y)
print("x != y", x != y)
print("x > y", x > y)
print("x < y", x < y)
print("x >= y", x >= y)
print("x <= y", x <= y)
print("1 < x < 10", 1 < x < 10)
print("1 < x and x < 10", 1 < x and x < 10)

print("\nOPERATORS: Identity")
# Identity operators are used to compare the objects, not if they are equal,
#  but if they are actually the same object, with the same memory location:
# is      Returns True if both variables are the same object	    x is y	
# is not	Returns True if both variables are not the same object	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("x =", x)
print("y =", y)
print("z = x = ", x)
print("x is z", x is z)
print("x is not y", x is not y)
print("x == y", x == y)

print("\nOPERATORS: Membership")
# Membership operators are used to test if a sequence is presented in an object:
# in      Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y
fruits = ["apple", "banana", "cherry"]
print("fruits =", fruits)
print("\"banana\" in fruits", "banana" in fruits)
print("\"cherry\" not in fruits", "cherry" not in fruits)

text = "Hello World"
print("text =", text)
print("\"H\" in text", "H" in text)