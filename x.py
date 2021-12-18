message = "When you are ready to make your order - type 'quit'."
message += "\nPlease enter a topping for your pizza: "
topping = ""
toppings = []
x= "rgr"

while True:
    topping = input(message)
    if topping == 'quit':
        break
    print(f"We will add a {topping} to your pizzafhhrgrgrgrgrgrgrgrgrgrgrgrgrgrghhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh!")
    toppings.append(topping)

print(f"We'll make your pizza ready in a short time.\nSelected "
      f"toppings: {toppings}.")

if not not input():
    pass



