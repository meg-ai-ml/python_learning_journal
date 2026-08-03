# Set the target alien color for the current round
alien_colour = "pink"

# Award points only if the player encounters a pink alien.
if alien_colour == "green":
    print("You earned 5 points for shooting the alien.")

elif alien_colour == "yellow":
    print("You earned 10 points for shooting the alien.")
else:
    print("You earned 15  points for shooting the alien.")

# The user is presented with the else statement as the alien is neither green or yellow.
