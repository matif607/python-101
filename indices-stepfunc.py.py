parrot = "Norwegian Blue"
print(len(parrot))

print(parrot[0:6])
print(parrot[2:5])

#negative indices
print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[-4:2])

#step func
print(parrot[0:6:3])
print(parrot[:6:3]) #this line does'nt def start value so the code will start from index 0
print(parrot[0::3]) #this line doesn't def stop value so the code will execute till last value


print(parrot[14:1:-1])