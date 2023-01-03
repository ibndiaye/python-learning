import random


def ask_number(nb_min, nb_max):
    nb_int = 0
    while nb_int == 0:
        nb_str = input(f"enter number of choice between {nb_min} and {nb_max}? ")
        try:
            nb_int = int(nb_str)
        except:
            print("enter a valid number")
        else:
            if nb_max < nb_int or nb_int < nb_min:
                print(f"not in range")
                nb_int = 0
    return nb_int


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4

number = 0

for i in range(0, NB_LIVES):
    lives = NB_LIVES - i
    print(f"you have #{lives} lives")
    if lives == 0:
        print("you lost")
        break
    else:
        number = ask_number(MIN_NUMBER, MAX_NUMBER)
        if number > MAGIC_NUMBER:
            print("magic number is smaller")
            lives -= 1
        elif number < MAGIC_NUMBER:
            print("magic number is bigger")
            lives -= 1
        else:
            print("you won")
            break

# while number != MAGIC_NUMBER:
#     print(f"you have #{lives} lives")
#     if lives==0:
#         print("you lost")
#         break
#     else:
#         number = ask_number(MIN_NUMBER, MAX_NUMBER)
#         if number > MAGIC_NUMBER:
#             print("magic number is smaller")
#             lives-=1
#         elif number < MAGIC_NUMBER:
#             print("magic number is bigger")
#             lives -= 1
#         else:
#             print("you won")
