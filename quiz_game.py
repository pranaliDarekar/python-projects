#python quiz game

from ast import Add
from re import A
from urllib.response import addbase


questions = ( "How many elemts are there in the periodic table?: "
             ,"Which animal lays the largest eggs?:  "
             ,"What is the most abundant gas in the earths atmosphere?:  "
             ,"How many bones are there in the human body?:  "
             ,"What planet in the solar system is the hottest planet?:  ")

options = ( ("A. 116","B. 117","C. 118","D. 119 ")
           ,("A. Whale","B. Crocodile","C. Elephant","D. Ostrich")
           ,("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen")
           ,("A. 206","B. 207","C. 208","D. 209")
           ,("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers = ("C","D","A","A","B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the correct answers")


    question_num += 1

print("----------------------------")
print("         RESULTS            ")
print("----------------------------")

print("answers:", end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print("----------------------------")
total = int(score/ len(questions) * 100)
print(f"Your score is {total}%")