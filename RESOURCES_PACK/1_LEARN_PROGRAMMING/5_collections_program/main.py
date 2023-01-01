# collections : Arrays, Lists, Tuples...
# Tuples () : immutable : you cannot change it
# List [] : mutable : You can add/delete items or modify them
# multiple items

# ------------ TUPLES ------------
#            0        1       2        3
# persons = ("Brian", "Bob", "Alice", "Jean")  # Tuple
# print(len(persons))  # 0 to len()-1
# print(persons[-1])  # the last element

# for i in range(0, len(persons)):
#     print(persons[i])

# for i in persons:
#     print(i)
#     print(len(i))
#     print(i[-1])
#     print()

# values = range(0, 5)  # -> (0, 1, 2, 3, 4)
# print(values[-1])

# ---------- LISTS -----------
"""persons = ["Brian", "Bob", "Alice", "Jean"]
new_person = "David"

print(persons)

persons.append(new_person)
# persons[0] = "Steven"
del persons[1]

print(persons)

for i in persons:
    print(i)


def change_value(a):
    a[0] = 10


test = [1, 2, 3, 4]
print(test)
change_value(test)
print(test)"""

# ---------- TUPLES AND FUNCTIONS -----------

"""def get_informations():
    return "Alice", 20, 1.6


def display_information(name, age, height):
    print(f"Name: {name}, Age: {age}, Height: {height}")


infos = get_informations()
print(infos)
display_information(*infos)  # unpack tuple  infos[0], infos[1], infos[2]
# print(infos)
#
# print("Name: " + infos[0])
# print("Age: " + str(infos[1]))
# print("Height: " + str(infos[2]))


# name, age, height = get_informations()
# display_information(name, age, height)"""


# ---------- SLICES -----------
persons = ("Brian", "Bob", "Alice", "Jean", "Steve", "John")

# print(persons)
# [start:stop:step]
#for i in persons[:-1]:
#    print(i)

name = "Alice"
print(name[::-1])



