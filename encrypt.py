new_str = ""
n = input("Enter a string:  ")
for i in n:
    i = ord(i)+1
    #print(i)
    i = chr(i)
    #print(i)
    new_str = new_str + i
print(new_str)

