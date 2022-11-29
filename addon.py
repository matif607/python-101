from tkinter.ttk import Separator


number = input("please enter the number you like with separators: ")
separator = ""

for char in number:
    if not char.isnumeric():
        separator = separator + char
#print(separator)

values = "".join(char if char not in separator else " " for char in number).split()
print(sum[int(val) for val in values]))

