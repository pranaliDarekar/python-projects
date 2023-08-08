name = input("Type your name: ")
print("Welcome!",name, "to this adventure game.")

answer = input("You are on a dirt road,it has come to an end and you can go left or right, which way would you like to choose? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across it? Type walk to walk around or swim to swim across it: ").lower()
    
    if answer == "swim":
        print("You swam across the river and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. YOU LOSE!")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()
    
    if answer == "cross":
      answer = input("You crossed a bridge and meet a stranger. Do you want to talk to stranger? (YES/NO): ").lower()
      if answer == "yes":
            print("You talk to the stranger and they give you gold. You won!")

      elif answer == "no":
            print("You dont talk to the stranger and you lose")
      else:
            print("Not a valid option. You lose!")

    elif answer == "back":
      print("You go back and lose")

    else:
      print("Not a valid option. You lose!")      
   

else:
    print("Not a valid option. YOU LOSE!")

print("Thank for trying")



