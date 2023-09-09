# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# roulette = random.randint(0, len(names)) in this code if the program picks the last name then index will be -1 and it will give error
roulette = random.randint(0, len(names)-1)
print(roulette)

payee = (names[roulette])

print("{} is going to buy the meal today!".format(payee))

#this code is randomly going to pick the person who is going to buy meal
#All this can be replaced by one line code

roulette_2 = random.choice(names)
print("{} is going to buy meal today!".format(roulette_2))