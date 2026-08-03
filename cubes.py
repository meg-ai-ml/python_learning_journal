# Method 1 to create a list of cubes.

# Create empty list.

cubes = []

# Add value from 1 to 10.

for value in range(1,11):
    
    cube = value**3 # Cube every value from 1 to 10.
    
    print(cube) # Present all cubed values to user.
    
# Method 2 to create a list of cubes.

# Create a list which includes the for loop and the cube python operator.

cubes = [ value**3 for value in range(1,11) ]

print(cubes)
