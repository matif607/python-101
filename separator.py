number = "9,23,100 500:1200;2000"
separator = ""

for char in number:
    if not char.isnumeric():
        separator = separator + char
print(separator)