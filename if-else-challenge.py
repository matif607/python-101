answer = 5 
number = int(input())

if number == answer:
    print("well done, you guessed it 1st time")
else:
    if number < answer:
        print("guess higher")
    else:
        print("guess lower")
    number = int(input())
    if number == answer:
        print("well done, you got it")
    else:
        print("sorry that's incorrect")
