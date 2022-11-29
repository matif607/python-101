if __name__ == '__main__':
    n = int(input().strip())
    m = n-1
    arr = list(map(int, input().rstrip().split()))
    arr2 = arr[::-1] 
    print(*arr2, sep=" ")

# (a,b) = map(int, input().split(' '))
# print("A: ",a,"B: ",b)