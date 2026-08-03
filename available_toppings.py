available_toppings = ["mushrooms", "olives", "green peppers",
                      "pepperoni", "extra cheese", "jalepeno"]
requested_toppings = [ "mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding", requested_topping)
    else:
        print(f"Sorry! {requested_topping} is not available")
print("Finished making your pizza")

