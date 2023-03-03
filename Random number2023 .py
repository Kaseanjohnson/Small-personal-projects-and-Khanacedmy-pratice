import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        character += digits
    if special_characters:
        characters += special


    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = meets_criteria and special_characters
    return(pwd)



min_length = int(input("Enter your password: "))
has_number = input("Do you want to have numbers? (Y/N)").lower == "Y"
has_special = input("Do you want to have special characters? (Y/N)").lower == "Y"
pwd = generate_password(min_length, has_number, has_special)

print("the generated password is: ", pwd)