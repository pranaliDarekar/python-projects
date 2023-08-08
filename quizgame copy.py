score = 0
print("Welcome!! to my general knowleage quiz game")

playing = input("Do you want to play? ")

if playing != "Yes":
    quit()
print("Okay, Let's Start :)")


answer = input("Which is the tallest mountain in the world? ")

if answer.lower() == "Mount Everest":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which is the latitude that runs through the centre of the Earth?  ")

if answer.lower == "Equator":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which is the largest desert in the world? ")

if answer.lower() == "Sahara Desert":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which country has the highest population?  ")

if answer == "China":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

answer = input("Which is the largest waterfall in the world? ")

if answer == "Victoria Falls":
    print("Correct!")
    score += 1
else :
    print("Incorrect!")

print("You got " +str(score)+ " questions correct!")
print("You got " +str((score/4)* 100)+ " %. ")