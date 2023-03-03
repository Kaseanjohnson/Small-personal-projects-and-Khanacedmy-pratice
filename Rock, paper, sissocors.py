import random

user_wins = 0
computer_wins = 0

options = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("type rock/paper/scissors or q to quit: ").upper()
    if user_input == "Q":
        break

    if user_input not in ["Rock", "Paper", "Scissors"]:
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "Rock" and computer_pick == "Scissors":
        print("you win.")
        user_wins += 1

    elif user_input == "Paper" and computer_pick == "Rock":
        print("you win!")
        user_wins += 1

    elif user_input == "Scissors" and computer_pick == "Paper":
        print("you win!")
        user_wins += 1
    else:
        print("you lost.")
        computer_wins += 1

print("you won", user_wins, "times.")
print("the computer won", computer_wins, "times")
print("see ya.")
