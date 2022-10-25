for i in range(1, 13):
    print("no. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
    print("no. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    #everything is left aligned

print()
print("pi is approximately {0:12}".format(22/7))
print("pi is approximately {0:12f}".format(22/7))
print("pi is approximately {0:<12.50f}".format(22/7))

name = "atif"
age = 25

pi = 22 / 7
print(f"pi is approxmately {22 / 7:12.50f} ")
print(f"pi is approximately {pi:12.50f} ")

print(name + f" is {age} years old")
print(name + age + "years old") # this will give error