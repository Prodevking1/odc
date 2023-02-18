from rest_connect import * 

def load_manager(name, price):
    req_db = MenuItem.get_by_name(name)
    if req_db == []:
        item = MenuItem(name, price)
    else:
        item = MenuItem(name, req_db[0][2])
    return item

def add_item_to_menu():
    while True:
        inp_n = input("Enter an item name : ")
        if inp_n == '': 
            print("Should not be empty!")
            continue
        if MenuItem.get_by_name(inp_n) != []:
            print("Item already exists!")
            continue
        break
    while True:
        inp_p = input("Enter a price : ")
        try:
            p = int(inp_p)
        except:
            continue
        if p < 0:
            continue
        break
    item = load_manager(inp_n, p)
    item.save()

def remove_item_from_menu():
    while True:
        inp_n = input("Enter an item name : ")
        if inp_n == '': 
            print("Should not be empty!")
            continue
        if MenuItem.get_by_name(inp_n) == []:
            print("Item does not exists!")
            continue
        break
    item = load_manager(inp_n,0)
    item.delete()

def update_item():
    while True:
        inp_n = input("Enter an item name : ")
        if inp_n == '': 
            print("Should not be empty!")
            continue
        if MenuItem.get_by_name(inp_n) == []:
            print("Item does not exists!")
            continue
        break
    while True:
        inp_p = input("Enter new price : ")
        try:
            p = int(inp_p)
        except:
            continue
        if p < 0:
            continue
        break    
    MenuItem.update(inp_n, p)

def show_restaurant_menu():
    print("\nRestaurant Menu\n===============")
    for id, n, p in MenuItem.all():
        print(n, p)
    

def show_user_menu():
    while True:
        print("\n       MENU")
        print("(a) Add an item")
        print("(d) Delete an item")
        print("(u) Update an item price")
        print("(v) View the menu")
        print("(x) Exit")
        sel = input(" : ")
        if sel in ('x', 'X'):
            show_restaurant_menu()
            print("\nExiting program. Goodbye.\n")
            break
        if sel in ('a', 'A'):
            add_item_to_menu()
        elif sel in ('d', 'D'):
            remove_item_from_menu()
        elif sel in ('v', 'V'):
            show_restaurant_menu()
        elif sel in ('u', 'U'):
            update_item()

show_user_menu()