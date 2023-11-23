def sum_eo(n, t):

    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


solution = sum_eo(11, 'e')
print(solution)