import sys
def getint(prompt):
    """This function will get 2 integers and divide 1st by second"""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number. Please type again ")
        except EOFError:
            sys.exit(1)
        finally:
            print("finally block always executes")


first_number = getint("pLease enter 1st number: ")
second_number = getint("Please enter second number: ")

try:
    print(f"{first_number} divided by {second_number} is {first_number / second_number}")
except ZeroDivisionError:
    print("You cannot divide by 0")
    sys.exit(2)
else:
    print("Division performed successfully")


