alphabets = 'abcdefghijklmnopqrstuvwxyz'

backwards = alphabets[25:0:-1]
backwards_l = alphabets[25::-1] # to include the last alphabet
#backwards_l1 alphabets[::-1]
##bkwd = alphabets[25:-1:-1] # this wont work
print(backwards)
print(backwards_l)
#print(backwards_l1)
#print(bkwd)

today = "friday"

print("day" in "today")