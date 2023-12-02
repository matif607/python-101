choice = '_'



while choice != 0:
    if choice in '12345':
        print(f'You chose {choice}')
    else:
        print("please chose from the option below")
        print('1: learn python')
        print('1: learn java')
        print('1: learn golang')
        print('1: learn C++')
    number_selected = int(input("Please select a number from 1 to 5: "))

