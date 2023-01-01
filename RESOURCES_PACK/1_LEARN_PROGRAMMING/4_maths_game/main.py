import random

MIN_NUMBER = 1
MAX_NUMBER = 100
NB_QUESTIONS = 10


def ask_question():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0, 1)
    # 0 -> +
    # 1 -> *
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    answer_str = input(f"Compute: {a} {operator_str} {b} = ")
    answer_int = int(answer_str)
    compute = a+b
    if o == 1:
        compute = a*b
    if answer_int == compute:
        return True

    return False


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} out of {NB_QUESTIONS}:")
    if ask_question():
        print("Right answer")
        nb_points += 1
    else:
        print("Wrong answer")
    print()


# Your points : 2 out of 4
print(f"Your points : {nb_points} out of {NB_QUESTIONS}")

adverage = int(NB_QUESTIONS/2)
if nb_points == NB_QUESTIONS:
    print("Excellent!")
elif nb_points == 0:
    print("Improve your maths!")
elif nb_points > adverage:
    print("Good!")
else:
    print("You can do better")

