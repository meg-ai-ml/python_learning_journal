age = 19

# Check if the person is eligible to vote.

if age >= 18:
    print("You are old enough to vote!") # Prints the message because 19 is greater than 18.
  
age = 17

# Check if the person is eligible to vote.

if age >= 18:
    print("You are old enough to vote!") # Skips the message because 17 is lesser than 18.
    print("Have you registered to vote?") # Skips the message because 17 is lesser than 18.

# Check if the person is ineligible to vote.
    
else:
    print("Sorry! You are too young to vote") # Prints the message because 17 is lesser than 18.


