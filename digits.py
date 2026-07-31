"""
digits.py - Numerical List Aggregations with range(), min(), max(), and sum()

This script demonstrates basic mathematical operations on Python lists:
- Generating stepped numerical sequences using range(start, stop, step)
- Finding minimum and maximum values with min() and max()
- Calculating total sums with sum() on integer and float lists
"""




digits = list(range(1,1001,5))
print("This is the minimum digit in this list ",min(digits))
print("This is the maximum digit in this list ",max(digits))
print("This is the sum of the digits in this list ",sum(digits))

floats = [1.0, 111.25, 99.9, 0.1,225.50]
print("This is the minimum digit in this list ",min(floats))
print("This is the maximum digit in this list ",max(floats))

