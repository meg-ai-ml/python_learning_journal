"""
cubes.py - Generating Numerical Lists and List Comprehensions

This script demonstrates two ways to construct numerical lists in Python:
- Using a standard `for` loop with range() and exponentiation (**3)
- Using a concise, idiomatic Python list comprehension
"""


cubes = []
for value in range(1,11):
    cube = value**3
    print(cube)

cubes = [ value**3 for value in range(1,11) ]
print(cubes)
