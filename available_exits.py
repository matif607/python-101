availabe_exits = ["east", "west", "north", "south"]

chosen_exit = ""

while chosen_exit not in availabe_exits:
    chosen_exit = input("please chose a direction: ")
    if chosen_exit == "quit":
        print("game over")
        break

print("aren't you glad you are out of there")