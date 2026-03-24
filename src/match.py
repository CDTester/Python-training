import datetime
# MATCH - similar to switch in other languages
print("MATCH")
day = datetime.datetime.now().strftime("%w")
print("day = ", day, type(day))
match day:
  case "0":
    print("Sunday")
  case "1":
    print("Monday")
  case "2":
    print("Tuesday")
  case "3":
    print("Wednesday")
  case "4":
    print("Thursday")
  case "5":
    print("Friday")
  case "6":
    print("Saturday")
  case _:
    print("you are no longer in the current spacetime continuum")

match day:
  case "1" | "2" | "3" | "4" | "5":
    print("Today is a weekday")
  case "6" | "7":
    print("I love weekends!")