# Create a list of cars.
cars = [ "audi", "BMw", "subaru" , "toyota" ]

# Create the loop.
for car in cars:

    # Present the car in uppercase if said to.
    
    if car.lower() == "bmw" :
        print(car.upper())
        
    # Present the car in title case if said do.    
    else:
        print(car.title())

