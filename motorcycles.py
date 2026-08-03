otorcycles = [ 'honda','yamaha','suzuki' ]

print(motorcycles)

motorcycles[0] ='ducati'

print(motorcycles)

motorcycles[0] = 'honda'
print(motorcycles)

motorcycles.append('ducati')

print(motorcycles)

motorcycles = []

print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(1, 'ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

popped_motorcycle = motorcycles.pop(0)
print(popped_motorcycle)

print(motorcycles)

motorcycles.append('honda')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.remove("honda")
print(motorcycles)





