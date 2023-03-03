
is_male = False
is_short = True

if is_male and is_short:
    print("you are a male and tall")
elif is_male and not(is_short):
    print("you are a tall male")
elif not(is_male) and is_short:
    print("you are not a male and short ")
else:
    print("you are not a male and short")