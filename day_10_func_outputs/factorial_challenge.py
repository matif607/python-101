def factorial(n: int) -> int:
    """return n factorial"""
    if n <= 1:
        return 1

    result = 2
    for x in range(3, n + 1):
        result *= x
    return result


for i in range(4):
    print(factorial(i))