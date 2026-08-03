pizzas = [ "Veg Exocita" , "Chicken Shawarma", "Indo Tandoori Paneer Tikka"]
for pizza in pizzas:
    print("I like " + pizza)
print('I really love pizza!')

friends_pizzas = pizzas[:]
print(friends_pizzas)

pizzas.append("Pepperoni")
print(pizzas)

friends_pizzas.append("Margherita")
print(friends_pizzas)

print("My favourite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")
for friend_pizza in friends_pizzas:
    print(friend_pizza)


