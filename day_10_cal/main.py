from art import logo
print(logo)

#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  '+': add,
  '-': substract,
  '*': multiply,
  '/': divide
}
def calculator():
  num1 = int(input("type first number:"))
  
  for symbol in operations:
    print(symbol)

  should_continue = True
  while should_continue:
    operation_symbol = input("pick an operation: ")
    num2 = int(input("type another number:"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer} ")
    if input(f"type 'y' to continue calculating with {answer}, type 'n' to start again:\n") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()