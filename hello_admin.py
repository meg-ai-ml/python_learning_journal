usernames = [ "megha", "meghan", "meghna"]
admin_list = [ "meg", "meghana"]
if usernames:
    for username in usernames:
        print("Welcome", username)
if admin_list:
    for admin in admin_list:
        print(f"Hello {admin}, would you like a status report")
else:
    for username in usernames:
        print(f"Hello {username} , thank you for logging in again")
     
