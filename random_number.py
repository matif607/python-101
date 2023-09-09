# import random
# number = random.randint(0, 10)
# print(number)

n = 5

for i in range(n):
  for j in range(i):
    print('* ', end='')
  print('')  

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end='')
    print('')


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary)
