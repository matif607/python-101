# 1. ADD
# 2. SUBTRACT
# 3.MULTIPLY
# 4.DIVIDE

print("select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("3. DIVIDE")

operation = input()
if operation == "1":
    num1 = int(input("Enter 1st numer: "))
    num2 = int(input("Enter 2nd number: "))
    print("the sum is: ", num1 + num2)
elif operation == "2":
    num1 = int(input("Enter 1st numer: "))
    num2 = int(input("Enter 2nd number: "))
    print("the subtraction is: ", num1 - num2)
elif operation =="3":
    num1 = int(input("Enter 1st numer: "))
    num2 = int(input("Enter 2nd number: "))
    print("the multiplication is: ", num1 * num2)
elif operation == "4":
    num1 = int(input("Enter 1st numer: "))
    num2 = int(input("Enter 2nd number: "))
    print("the division is: ", num1 / num2)
else:
    print("invalid entry")