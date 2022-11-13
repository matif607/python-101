name = input("Enter your name: ")
age = int(input())

if 18 <= age <= 31:
    print("welcome to the party {} ".format(name))
else:
    print("go fuck yourself", name)