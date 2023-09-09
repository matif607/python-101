choice = "-"
while choice != "0":
    if choice in "12345":
        print("you chose {}".format(choice))
    else:
        print("Please choose your options from below: ")
        print("1: \t pen")
        print("2: \t pencil")
        print("3: \t notebook")
        print("4: \t book")
        print("5: \t you hav not chosen anything")
    
    choice = input() 



# stationary = ['pen', 'pencil', 'eraser', 'refill', 'sharpner', 'ruler', 'compass', 'roller', 'notebook', 'diary']
# if choice == 1:
#     print("You have selected ", stationary[0], "as the option")
