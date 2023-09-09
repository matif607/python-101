value = 8
answer = 0
 
for x in range(1, 13):
    answer = value * x
    print("{0} times {1} is {2}".format(x, value, answer))



asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]
 
for asteroid in asteroids:
    if asteroid == 9617:
        print("Grahamchapman")
    elif asteroid == 9618:
        print("Johncleese")
    elif asteroid == 9619:
        print("Terrygilliam")
        break
    elif asteroid == 9620:
        print("Ericidle")
    elif asteroid == 9621:
        print("Michaelpalin")
    else:
        print("Terryjones")
else:
    print("MontyPython")

for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)


choice = None
 
while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        break
 
    print("You have selected {}".format(choice))
else:
    print("Thank you for playing, please call back soon.")