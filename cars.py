"""
cars.py - Sorting Methods and List Utility Functions

This script demonstrates Python list sorting techniques:
In-place permanent sorting with .sort() (ascending & descending)
Out-of-place temporary sorting with the built-in sorted() function
Reversing list order with .reverse()
Finding list size using the len() function

"""

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]

print(cars)

print('Sorting the cars')

cars.sort()
print(cars)

cars.sort(reverse = True )
print(cars)

cars = [ 'bmw', 'audi', 'toyota', 'subaru' ]
print("Here is the sorted list")
sorted_cars = sorted(cars)
print(sorted_cars)
print("Here is the original list")
print(cars)

cars.reverse()
print(cars)

print("The length of this list is ", len(cars))

