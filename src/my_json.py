import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
print("\nParse string to json using json.loads(string)")
y = json.loads(x)

# To string
print("\nConvert json to string using json.dumps(json)")
print(json.dumps(y,indent=4))

# the result is a Python dictionary:
print(y["age"])


people = {
  "person1": {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
      {"model": "BMW 230", "mpg": 27.5},
      {"model": "Ford Edge", "mpg": 24.1}
    ]
  },
  "person2": {
    "name": "Dave",
    "age": 25,
    "married": False,
    "divorced": False,
    "children": (),
    "pets": None,
    "cars": [
      {"model": "Skoda Enyaq", "m/KWh": 4.5}
    ]
  }
}

print(json.dumps(people))