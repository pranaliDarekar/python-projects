import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number larger than 0!")
        quit()
else:
    print("Please enter a number! ")
    quit()
    
random_number = random.randint(0,top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time")
        continue6
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("you were above the number!")
    else:
            print("you were below the number")

print("you got it in", guess, "guesses")

