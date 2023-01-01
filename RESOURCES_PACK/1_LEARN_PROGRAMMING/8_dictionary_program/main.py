# --- PART 1 ---
"""person = {"name": "Paul", "age": 25, "height": 1.75}
# print(person["name"])
# print(person["age"])
person["name"] = "Brian"
person["job"] = "Developer"
person["purchases"] = ("chocolate", "butter", "cheese")
for i in person:
    # print(i)
    # print(person[i])
    print(f"key: {i} - value: {person[i]}")"""

# --- PART 2 ---

# name, age, height
persons = [
    ("Alice", 25, 1.6),
    ("Brian", 35, 1.8),
    ("Paul", 29, 1.75),
    ("Martin", 32, 1.7)
]

def get_infos(name, l):
    for i in l:
        if i[0] == name:
            return i
    return None


infos = get_infos("Paul", persons)
# print(infos)

persons_dict = {
    "Alice": (25, 1.6),
    "Brian": (35, 1.8),
    "Paul": (29, 1.75),
    "Martin": (32, 1.7)
}

infos = persons_dict.get("Marc")
if not infos:
    print("Key not found")
else:
    print(infos)

