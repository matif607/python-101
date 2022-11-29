# n = int(input())
# for i in range(n):
#     if i % 2 != 0 and 1 < i <= 5:
#         print("Weird")
#     else:
#         print("Not Weird")
# for i in range(n):
#     if i % 2 == 0 and 6 <= i <= 20:
#         print("Weird")
# for i in range(n):
#     if i % 2 == 0 and i > 20:
#         print("Not Weird")


# Objective
# In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.

# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Sample Input 1

# 24
# Sample Output 1

# Not Weird
# Explanation

# Sample Case 0: 
#  is odd and odd numbers are weird, so we print Weird.

# Sample Case 1: 
# n > 20 and  is even, so it is not weird. Thus, we print Not Weird.


n = int(input("please a enter an int here: "))
# print(n)

# if n % 2 != 0 and 2 < n <= 5:
#     print("Weird")
# elif n % 2 != 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 != 0 and n > 20:
#     print("Weird")
# else:
#     print("Not Weird")

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 1 < n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
