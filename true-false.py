# day = "Monday"
# temp = 30
# raining = True

# if day == "Saturday" and temp == 27 and not raining:
#     print("go swimming")
# else:
#     print("learn python")

# print()

# day = "Saturday"
# temp = 30
# raining = True

# if day == "Saturday" and temp == 27 and not raining:
#     print("go swimming")
# else:
#     print("learn python")

# print()

# day = "Saturday"
# temp = 27
# raining = True

# if day == "Saturday" and temp == 27 and not raining:
#     print("go swimming")
# else:
#     print("learn python")

# print()

# day = "Saturday"
# temp = 27
# raining = True

# if (day == "Friday" and temp == 27) or not raining:
#     print("go swimming")
# else:
#     print("learn python")

# print()

# day = "Saturday"
# temp = 27
# raining = False

# if (day == "Friday" and temp == 27) or not raining:
#     print("go swimming")
# else:
#     print("learn python")

#always use parenthesis while using and & or together

# nl = []
# for i in range(1500, 2701):
#   if i % 7 == 0 and i % 5 == 0:
#     nl.append(str(i))
# print(','.join(nl))

# temp = input("temparature you would like to convert: ")
# degree = int(temp[: -1])
# i_convention = [-1]

# if i_convention.upper() == 'C':
#   result = int(round((9 * degree) / 5 + 32))
#   o_convention = 'F'
# elif _convention.upper() == 'F':
#   result = int(round((degree - 32) * 5 / 9))
#   o_convention = 'C'
# else:
#   print("invalid convention")
#   quit()

# print("the result in", o_convention, "is", result, 'degrees.')

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1]) # -1 after colon means excluding the last char which is alphabet here
i_convention = temp[-1] # taking the last character

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")