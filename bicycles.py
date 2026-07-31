"""

bicycles.py - List Indexing & Basic String Formatting

This script demonstrates working with Python lists:
Accessing list elements using positive and negative indices.
Applying string methods like .upper() on list items.
Combining list items with strings using f-strings and print arguments.

"""

#Using the list function to list different types of bicycles
bicycles = [ "atlas","ladybird","hero","rockrider"]
print(bicycles) # ['atlas', 'ladybird', 'hero', 'rockrider']. 

# Listing names of different bicycles using index method.
print(bicycles[0]) # atlas
print(bicycles[3]) #rockrider
print(bicycles[2].upper()) # HERO
print(bicycles[-1]) # rockrider
print(bicycles[-2]) # hero

# Printing a message including a certain bicycle using an index method.

message = f"My first bicycle is a {bicycles[0]}"
print(message) # My first bicycle is a atlas

