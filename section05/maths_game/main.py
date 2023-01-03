import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTIONS = 4


def ask_number(nb_min, nb_max):
    a = random.randint(nb_min, nb_max)
    b = random.randint(nb_min, nb_max)
    c = random.randint(0, 1)
    op_str = "+"
    if c == 1:
        op_str = "*"
    result_str = input(f"what is {a} {op_str} {b}: ")
    result = int(result_str)
    compute = a + b
    if c == 1:
        compute = a * b
    if result == compute:
        return True
    return False


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n#{i + 1}")
    if ask_number(MIN_NUMBER, MAX_NUMBER):
        print("correct")
        nb_points += 1
    else:
        print("incorrect")
    print()

print(f"Your points out of {NB_QUESTIONS}: {nb_points} out of {NB_QUESTIONS}")
average = int(NB_QUESTIONS / 2)
if nb_points == NB_QUESTIONS:
    print("excellent")
elif nb_points == 0:
    print("improve your maths")
elif nb_points > average:
    print("good")
else:
    print("you can do better")
