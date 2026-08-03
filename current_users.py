current_users = [ "Bob", "Nick", "Ned", "Tom", "Rick", "BOB", "NICK", "NED", "TOM", "RICK", "bob", "nick","ned","tom","rick"]
new_users = [ "Tim", "tom", "Ned", "Greg", "Sam"]
for user in new_users:
    if user in current_users:
        print("The username is already taken")
        print("Enter a new username")
    else:
        print("This username is available")

