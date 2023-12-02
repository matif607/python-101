answer = 5
print("please guess a number between 1 and 10: ")
#number = int(input())

#best so far in this code

while True:
    number = int(input())
    if number == answer:
        print("Great!!")
        break
    elif number < answer:
        print("Guess Higher")
    else:
        print("Guess lower")


#slightly better

# if number != answer:
#     if number < answer:
#         print("guess higher")
#     else:   #if the guess is higher than answer
#         print("guess lower")
#     number = int(input())
#     if number == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry you have guessed wrong")
# else:
#     print("well done, you got it in 1st time")

 
 #most basic code


# if number < answer:
#     #print("guess higer")
#     #guess = int(input())
#     # if guess == answer:
#     #     print("well done, you guessed it")
#     print(int(input("guess higher: ")))
#     if number == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry you guessed incorrectly")
# elif number > answer:
#     #print("guess lower")
#     #guess = int(input())
#     # if guess == answer:
#     #     print("well done, you guessed it")
#     print(int(input("guess lower: ")))
#     if number == answer:
#         print("well done, you guessed it")
#     else:
#         [print("sorry you guessed incorrect")]
# else:
#     print("congrats, you got it")


def sum_eo(n, t):
    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

print(sum_eo(12, 'o'))