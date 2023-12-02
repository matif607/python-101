a = b = c = d = e = f = 12
print(c)

x, y, z = 11, 2, 76

print(x)
print(y)
print(z)

# the above example is called tuple

print("unpacking tuple")
data = 11, 2, 76
x, y, z = data

print(x)
print(y)
print(z)

# x, y, z looks like a tuple but they are not. they get thier values from the data tuple


print("unpacking list")
data_list = [5, 25, 75]
data_list.append(50)
# the above program will fail as the values are more than the variable
# if the above example was a tuple then program would not crash as we cannot append to a tuple
x, y, z = data_list
print(x)
print(y)
print(z)

