name = input("Enter your name: ")
age = int(input("how old are you {0} ".format(name)))

if age >= 18:
    print("you are eligible to vote")
else:
    print("come back in {0} years".format(18 - age))