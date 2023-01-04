# def custom_sort(e):
#    return len(e)

def display(collection, n_first_elements = -1):
    # title "----- PIZZAS (4) -----
    # display pizzas 1 pizza = 1 line
    # "NO PIZZAS"
    # collection.sort(reverse=True, key=custom_sort)
    c = collection
    if not n_first_elements == -1:
        c = collection[:n_first_elements]

    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("NO PIZZAS")
        return

    print(f"----- PIZZAS ({nb_pizzas}) -----")
    for i in c:
        print(i)
    print()
    print("first pizza : " + c[0])
    print("last pizza : " + c[-1])

def add_user_pizza(collection):
    p = input("Add your pizza :")
    #if pizza_exists(p, collection):
    if p.lower() in collection:
        print("ERROR : This pizza already exists")
    else:
        collection.append(p)


# def pizza_exists(e, collection):
#     for i in collection:
#         if e == i:
#             return True
#     return False

# pizza_exists(...) -> Bool
#   True -> pizza exists -> Print("ERROR : This pizza already exists")
#   False -> append


pizzas = ["4 cheeses", "vegetarian", "hawai", "calzone", "four seasons"]

# empty = ()

add_user_pizza(pizzas)
display(pizzas)
