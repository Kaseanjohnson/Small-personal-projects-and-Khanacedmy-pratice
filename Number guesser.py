import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("type a number greater than Zero.")
        quit()
else:
    print("please type in a number.")
    quit()


random_number = (random.randint(0, top_of_range))
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number.")
        continue

    if user_guess == random_number:
        print("you got it!")
        break

    else:
       if user_guess > random_number:
           print("you were above the number!")
       else:
           print("you were blew the number!")

print("you got in", guesses, "guesses")

