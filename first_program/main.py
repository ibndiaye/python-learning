# display_person_info
# Parameters : name, age
def display_person_info(name, age, height=0):
    print()
    print("Your name is " + name + ", you are " + str(age) + " years old")
    # print(f"Your name is {name}, you are {age} years old")
    # print("Your name is %s, you are %s years old" % (name, age))


    print("Soon you will be " + str(age + 1))

    # == equality
    # >  >=
    # <  <=
    # bool : True/False
    # age == 17 : You are almost an adult
    # age == 18 : You are now an adult : congrats!
    # elif -> else if
    # age > 60 : You are senior
    # age < 10: You are a kid
    # age >= 10 and age < 18 => Teenager
    #        10 <= age < 18
    #
    # age == 1 or age == 2 => Baby
    if age == 17:
        print("You are almost an adult")
    elif 10 <= age < 18:
        print("You are a teenager")
    elif age == 1 or age == 2:
        print("You are a baby")
    elif age == 18:
        print("You are now an adult : congrats!")
    elif age > 60:
        print("You are senior")
    elif age < 10:
        print("You are a kid")
    elif age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

    if not height == 0:
        print("Your height: " + str(height) + "m")




def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is your name? ")
    return name_answer


def ask_for_the_age(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " what is your age? ")
        try:
            age_int = int(age_str)
        except:
            print("ERROR: Age must be a number")
    return age_int


# ask for the name
#name1 = ask_for_the_name()
#name2 = ask_for_the_name()
# name1 = "foo1"
# name2 = "foo2"

# ask for the age
# age1 = ask_for_the_age(name1)
# age2 = ask_for_the_age(name2)

# Display the results
# display_person_info(name1, age1)
# display_person_info(name2, age2)

NB_PERSONS = 1

for i in range(0, NB_PERSONS):
    name = "foo" + str(i+1)
    age = ask_for_the_age(name)
    display_person_info(name, age, 1.6)

print("""A first line
    I can write
        what
            I want
""")

print("first", 5, 5.99, "last")

