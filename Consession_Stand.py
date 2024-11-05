# Consession stand Program




from zmq import NULL


menu = {"pizza" : 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("--------------------Menu---------------------")
for key,value in menu.items():
    print(f"{key:10}:  ${value:.2f}")
print("---------------------------------------------")

while True:
    item = input("Enter food in your cart (q to Quit):  ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)

print("--------- YOUR ORDER ---------")
for item in cart:
    total += menu.get(item)
    print (item, end=" ")

print()
print(f"Total is: ${total:.2f}")
print("------------------------------")    


