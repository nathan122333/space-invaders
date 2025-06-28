import random

print(" Nathan geuss the number for me please")
print("Nathan is thinking for a number from 1-10")
print("you have 3 chances to geuss correctly")
#user chooses a number
magic_number = random.randint(5,10)
#first guess
geuss1 = int(input("try 1: what is your geuss"))
if geuss1 == magic_number:
    print("you geussed it correct!")
else:
    geuss2 = int(input("try 2: geuss again"))
    if geuss2 == magic_number:
        print("YES!you geussed it in your second try")
    else:
        geuss3 = int(input("try 3: geuss again"))
        if geuss3 == magic_number:
            print("YES!you geussed it in your third try")

        else:
            print("Oh no, then number was{magic_number}")



