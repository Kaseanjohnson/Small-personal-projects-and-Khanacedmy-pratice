
hidden_word = "kasean"
guess = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False

while guess != hidden_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_guesses: True

if out_of_guesses:
    print("you lose")

else:
    print("you win")