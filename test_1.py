# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# (map[1][2]) = "X"
# print(map)
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal - 1] = 'X'

# 1st digit is vertical_column positions and 2nd is horizontal
# map[x][y]='X'



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")