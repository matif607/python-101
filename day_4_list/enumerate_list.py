for index, part in enumerate("abcdefgh"):
    print(index +1, part)

for t in enumerate("abcdefgh"):
    index, character = t # t is (0, 'a), (1, b) and so on
    print(index, character)

index, character = (0, "a")
print(index)
print(character)