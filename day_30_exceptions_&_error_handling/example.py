def factorial(n):
    # n! can also be defined as n * (n-1)
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(900))
except RecursionError:
    print("This program cannot print factorials that large")

