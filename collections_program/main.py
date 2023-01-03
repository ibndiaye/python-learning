persons = ("brian", "bob", "alice","jean") #tuple
persons = ["brian", "bob", "alice","jean"] #list
# print(len(persons))
# print(persons[-1])

# for i in range(0, len(persons)):
#     print(persons[i])

# for i in persons:
#     print(i)
#     print(len(i))
#     print(i[-1])
#     print()

# new_persons="david"
# print(persons)
# persons.append(new_persons)
# print(persons)
# del persons[0]
# print(persons)
#
# def change_value(a):
#     a[0] =10
#
#
# test=[1,2,3,4]
# print(test)
# change_value(test)
# print(test)

# def get_informations():
#     return "alice",20,1.6
#
# def display_info(name,age,height):
#     print(f"name: {name}, age: {age}, height: {height}")
#
# name,age,height = get_informations()
# info = get_informations()
# display_info(name,age,height)
# display_info(*info)

persons = ("brian", "bob", "alice","jean","steve","john") #tuple

print(persons)

for i in persons[::2]:
    print(i)

name="alice"
print(name[::-1])