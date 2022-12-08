# solution without using continue function
# for i in range(20):
#     if i % 3 != 0 and i % 5 != 0:
#         print(i)

#solution using continue
for i in range(21):
    if i % 3 ==0 or i % 5 == 0:
        continue
    print(i)