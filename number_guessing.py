# Python number guessing game

from curses.ascii import isdigit
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
is_running = True
guesses = 0

print("----------------------------------")
print("PYTHON NUMBER GUESSING GAME !!")
print("Select a number between 1 to 100")
print("----------------------------------")
print()

while is_running:
    guess = input("Enter a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < 1 or guess > 100:
            print("Out of Range!")
            print("Please enter a number between 1 to 100")
        elif guess > answer:
            print("Too High! Try again!!")
        elif guess < answer:
             print("Too Low! Try again!!")
        else:
            print("CORRECT!!")
            print(f"The answer was: {answer}")
            is_running = False

    else:
        print("Invalid guess!!")
        print("Please enter a number between 1 to 100")