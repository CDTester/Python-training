import re
print("\nREGEX:")

txt = "The rain in Spain falls mainly in the plane"
print("txt = ", txt)


print("\nFindall:")

print("[a-z] = look for pattern containing characters a-z. This will not include uppercase characters")
az = re.findall("[a-z]", txt)
print("az = re.findall(\"[a-z]\", txt) =", az)

print("\n[1-9] = look for pattern containing numbers 1-9.")
num = re.findall("[1-9]", txt)
print("num = re.findall(\"[1-9]\", txt) =", num)

print("\n^ = starts with")
startTrue = re.findall("^The", txt)
startFalse = re.findall("^the", txt)
print("startTrue = re.findall(\"^The\", txt) =", startTrue)
print("startFalse = re.findall(\"^the\", txt) =", startFalse)

print("\n$ = ends with")
endsTrue = re.findall("plane$", txt)
endsFalse = re.findall("the$", txt)
print("endsTrue = re.findall(\"plane$\", txt) =", endsTrue)
print("endsFalse = re.findall(\"the$\", txt) =", endsFalse)

print("\n. = any character")
without_dot = re.findall("h", txt)
with_dot = re.findall(".h.", txt)
print("many = re.findall(\"h\", txt) =", without_dot, " = T[h]e rain in Spain falls mainly in t[h]e plane")
print("many = re.findall(\".h.\", txt) =", with_dot, " = [The] rain in Spain falls mainly in [the] plane")


print("\n* = Zero or more occurences")
without_star = re.findall("f...s", txt)
with_star = re.findall("f.*s", txt)
print("many = re.findall(\"f...s\", txt) =", without_star, " = The rain in Spain [falls] mainly in the plane")
print("many = re.findall(\"f.*s\", txt) =", with_star, " = The rain in Spain [falls] mainly in the plane")

(r"\Bin\w+", txt)
print("\nSearch:")
print("\\b - Returns a match where the specified characters are at the beginning or at the end of a word")
print("\\B - Returns a match where the specified characters are NOT at the beginning or at the end of a word")
print("\\s - Returns a match where the string contains a white space character")
print("\\w - Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, _)")
findall = re.findall("\\w+in\\b", txt)
search = re.search("\\w+in\\b", txt)
print("\n\\w+in\\b = Where 'in' is part a word and it is at the beginning or end of the word")
print("findall = re.findall(\"\\w+in\\b\", txt) =", findall)
print("search = re.search(\"\\w+in\\b\", txt) =", search)
print("\nSearch provides a Match object. There are 3 methods you cn use with Match:")
print(".string - Returns the string that was searched = ", search.string)
print(".span() - Returns a tuple containing the start and end position of the first occurence = ", search.span())
print(".group() - Returns the part of the string where there was a match = ", search.group())

x = re.search("\\s", txt)
print("The first white-space character (\\s) is located in position:", x.start())

print("\nSplit:")
split = re.split("\\s", txt)
split_once = re.split("\\s", txt, maxsplit=1)
print("split = re.split(\"\\s\", txt) =", split)
print("split_once = re.split(\"\\s\", txt, maxsplit=1) =", split_once)

print("\nSub:")
sub = re.sub("\\s", "_", txt)
sub_count = re.sub("\\s", "_", txt, count=3)
print("sub = re.sub(\"\\s\", \"_\", txt) =", sub)
print("sub = re.sub(\"\\s\", \"_\", txt, count=3) =", sub_count)

