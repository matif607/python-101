low = 1 
high = 1000

print("Guess a number between {} and {} ".format(low, high))
input("Press Enter to start")

guesses = 1

while low != high:
    guess = low + (high - low) // 2
    hi_lo = input("my guess is {}. Should I guess higher or lower or is my guess correct. Press h or l or c if my guess is correct".format(guess).casefold())

    if hi_lo == "h":
        low = guess + 1
        #user has guessed a lower number so next guess is 1 bigger than that number
    elif hi_lo == "l":
        high = guess - 1
        #user has guessed a higher number so next guess would be 1 lower
    elif hi_lo == "c":
        print("I guessed the number in {} guesses".format(guesses))
        break
    else:
        print("Please enter h or l or c")

    guesses = guesses + 1
else:
    print("you guessed {}".format(low))
    print("I got it in {} number of guesses".format(guesses))
