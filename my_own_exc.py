from random import choice


availabe_foods = ["milk - drink", "soup - chinese", "tandoori - starter", "haka noodles - chinese", "milkshake - drink", 
"mojito - drink", "fried rice - chinese", "water - drink", "coffee - drink", "manchurian - starter", "chicken 65 - starter",
"triple rice - chinese", "prawns - starter", "schezwan rice - chinese", "paneer fry - starter"]

current_choice = []
choice = []

starters =[]
drinks = []
chinese = []

tmp = ""

for food in availabe_foods:
    if "drink" in food:
        drinks.append(food)
    elif "starter" in food:
        starters.append(food)
    elif "chinese" in food:
        chinese.append(food)
#print(starters)

valid_choice = []

for i in range(1, len(starters) +1):
    valid_choice.append(str(i))
print(valid_choice)

#optimal solution is to write a while loop

while current_choice != 0:
    if choice == starters:
        for i in range(1, len(starters) + 1):
            



print("Starters")
for key, value in enumerate(starters):
    print("{0}: {1} ".format(key + 1, value))

print()

print("Drinks")
for key, value in enumerate(drinks):
    print("{0}: {1} ".format(key + 1, value))

print()

print("Chinese")
for key, value in enumerate(chinese):
    print("{0}: {1} ".format(key + 1, value))