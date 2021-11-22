groceries =  {
    "Costco": ["Fire Alarm", "Rotissere Chicken", "Milk"],
    "Home Depot": ["Tarp"],
}

def grocery_list():
    while (True):
        menu = input('''
Welcome to List maker!

Press 1 to make a shopping list
Press 2 to add to an existing shopping list
Press 3 to delete a shopping list
Press 4 to view all shopping lists

''')
        if menu == "1":
            new_list = input('''
What is the name of the store? ''')
            groceries[new_list] = []
            print(f"Store added: {new_list} !")
            print(groceries)
        elif menu == "2":
                what_list = input ('''
What list do you want to add to
    ''')
                add_item = input('''
What item do you want to add?
    ''')
                groceries[what_list] = add_item
                print(groceries)
        elif menu == "3":
                    delete_list = input('''
What list do you want to delete?
    ''')
                    if delete_list in groceries:
                         del groceries[delete_list]
        elif menu == "4":
                print(groceries)
        else:
            print("Pick a valid option")
grocery_list()