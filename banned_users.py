# Create a list of banned users.
banned_users = [ "Andrew", "Toby", "Tom" ]

# Select a particularuser. 
user = "mary jane"

#Check if she is not a banned user and if so, allow them to post a response.
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
