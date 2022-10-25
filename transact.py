amt = int(input())
while(amt !=0):
    if amt < 0:
        print("debit")
    else:
        print("credit")
    amt = int(input())
print("transaction aborted")
