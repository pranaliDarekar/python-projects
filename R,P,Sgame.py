# Rock paper scissor game
import random

option = ("rock","paper","scissors")
running = True

while running:

    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter rock, paper or scissor: ").lower()

    print(f"Player's choice: {player}")
    print(f"Computer's choice: {computer}")

    if player == computer:
        print("It is a tie!!")
    elif player == 'paper' and computer == 'rock':
        print("You win!!")
    elif player == "scissors" and computer == "paper":
        print("You win!!")
    elif player == "rock" and computer == "scissors":
        print("You win!!")
    else:
        print("You lose!!")
    
    play_again = input("Play again?: (y or n) ").lower()
    if play_again == "n":
        print(" Thank you!!")
        break
    else:
        continue