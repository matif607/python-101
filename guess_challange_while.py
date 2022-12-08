import random
highest = 10
answer = random.randint(1, highest) # this can be either hard coded value like 1, 10 or can be variable as here
print(answer) # TODO: Remove after testing

guess = int(input("Please enter a number here between 1 and {}:  ".format(highest)))
if guess == 0:
    print("Game over")
else:    
    while answer != guess:
        if guess < answer:
            guess = int(input("Please guess higher: "))
        else: 
            guess = int(input("Please guess lower: ")) 
    print("well done you guessed it")


# Solution by TIm of udemy

# guess = 0 # intializing the guess
# print(" please enter a number between 1 and 10: ")

# while guess != answer:
#     guess = int(input()) 
#     if guess == 0:
#         print("game over")
#         break 
#     if guess == answer:
#         print("well done you guessed it")
#         break
#     else:
#         if guess < answer:
#             print("guess higher")
#         else:
#             print("guess lower")

