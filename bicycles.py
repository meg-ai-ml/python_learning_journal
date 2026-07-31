# bicycles.py - List Indexing & Basic String Formatting

#This script demonstrates working with Python lists:
#Accessing list elements using positive and negative indices.
#Applying string methods like .upper() on list items.
#Combining list items with strings using f-strings and print arguments.

bicycles = [ "atlas","ladybird","hero","rockrider"]
print(bicycles)

# Name 
print(bicycles[0])
print(bicycles[3])
print(bicycles[2].upper())
print(bicycles[-1])
print(bicycles[-2])
message = f"My first bicycle is a {bicycles[0]}"
print(message)

names = [ "netra","anushri","keyuree","saanvi"]
print(names)
print("hello",names[0])
print("how are you",names[1])
print("hi",names[2])
print("howdy",names[3])

transport = [ 'car','bike','scooter']
print('i want a big',transport[0])
print('i want a small',transport[1])
print("i don't want a",transport[2])


