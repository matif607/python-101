parrot = "Norwegian Blue"

letter = input("Enter a letter here: ")

if letter in parrot:
    print("{} is in {} ".format(letter, parrot))
else:
    print("I dont need that letter")