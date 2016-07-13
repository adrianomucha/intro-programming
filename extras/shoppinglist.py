shopping_list = []

print ("""What should we pick up at the store? """)

def show_help():
    print("""
Enter 'HELP' to get help.
Enter 'DONE' to stop adding items.
Enter 'SHOW' to see your current list.
Enter 'AUTHOR' to see author of the program.
""")

def show_list():
    print("here you can see your items: ")
    for item in shopping_list:
        print(item)
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}, list now has {} items".format(new_item, len(shopping_list)))

def show_author():
    print("Adrian Mucha NYU, 2016")

show_help()

while True:
    new_item= input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue 
    elif new_item == 'AUTHOR': 
        show_author()
        continue

    add_to_list(new_item)

show_list()





