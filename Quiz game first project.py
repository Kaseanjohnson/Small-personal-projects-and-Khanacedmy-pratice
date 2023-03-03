print("Welcome to the game")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()
print("Okay, Let's play!")

answer = input("What color is the sky? ")
if answer.lower() == "blue":
    print("correct!")
    score += 1
elif answer != "blue":
    print("incorrect")


answer2 = input("what color is an apple? ")
if answer2.lower()== "red":
    print("correct!")
    score += 1

elif answer2 != "red":
    print("incorrect")

print("you got " + str((score/2) * 100 + '%.'))