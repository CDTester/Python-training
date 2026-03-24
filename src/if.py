if 5 > 2:
  # indentation has to be the same value in a block
  print("Five is greater than (>) two")
  print("In the same if statement as 'if 5 > 2'")

if "hello" == "hello": print("hello equals (==) hello")

if 1 != 2: print("1 does not equal (!=) 2")

if 10 < 20: print("10 is less than (<) 20")

if 10 <= 10: print("10 is less than or equal (<=) to 10")

if 10 >= 10: print("10 is greater than or equal (>=) to 10")

is_logged_in = True
if is_logged_in: print("is_logged_in = True")

zero = 0
empty_string = ""
if empty_string:
  print("empty string should not = True")
else:
  print("Zero (0), empty strings (""), None, and empty collections are treated as False.")


txt1 = "The best things in life are free!"
if "free" in txt1:
  print("Yes, 'free' is present in:", txt1)

txt2 = "The best things in life are free!"
if "expensive" not in txt2:
  print("No, 'expensive' is NOT present in :", txt2)

a = 200
b = 33
if b > a:
  print(f"b({b}) is greater than a({a})")
else:
  print(f"b({b}) is not greater than a({a})")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# ELIF : is Python's way of saying "if the previous conditions were not true, then try this condition"
print("\nELIF")
a = 33
b = 33
if b > a:
  print("if b is greater than a")
elif a == b:
  print("elif a and b are equal")
else:
  print("Else a is greater than b")

score = 89
print("WITH ELIF")
print(f"score = {score} which is a", end=" ")
if score >= 90:
  print("Grade: A", end=" ")
elif score >= 80:
  print("Grade: B", end=" ")
elif score >= 70:
  print("Grade: C, end=" "")
elif score >= 60:
  print("Grade: D", end=" ")

print("\nUSING JUST IF")
print(f"score = {score} which is a", end=" ")
if score >= 90:
  print("Grade: A", end=" ")
if score >= 80:
  print("Grade: B", end=" ")
if score >= 70:
  print("Grade: C", end=" ")
if score >= 60:
  print("Grade: D", end=" ")

# CONDITIONAL EXPRESSION - TERNARY OPERATOR
a = 2
b = 330
print("\n\nTernary operator")
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("A=B") if a == b else print("B")

# AND OR NOT
print("\nAND, OR, NOT")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

age = 25
is_student = False
has_discount_code = True
if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# NESTED IF
print("\nNested If")
x = 41
if x > 10:
  print("Above ten,", end=" ")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


age = 25
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

# PASS STATEMENT
print("\nPass Statement, if statement cannot be empty")
a = 33
b = 200
if b < a:
  pass # comments cannot be used instead
else:
  print("No options in if, so used pass")