from camelcase import CamelCase

print("\nPIP - is a package installer for python")
print("pip install camelcase")
print("packages can be found at https://pypi.org/")
print("This will install camelcase into your appdata\\local\\pip\\cache\\ folder")
print("This package can now be used by 'import camelcase'")

c = CamelCase()
txt = "hello world"
print("\ntxt =", txt)
print(c.hump(txt))

print("\nUninstall:")
print("pip uninstall camelcase")

print("\nUpgrade:")
print("pip install camelcase --upgrade")

print("\nList:")
print("pip list\n")
list = """Package   Version
--------- -------
camelcase 0.2
pip       26.0.1"""
print(list)
