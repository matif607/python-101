available_parts = ["Computer",
                    "monitor",
                    "mouse mat",
                    "mouse",
                    "keyboard",
                    "hdmi"
                    ]
current_choice = "-"
computer_parts = []

valid_choices = []
for i in range(1, len(available_parts)+ 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != "0":
    if current_choice in valid_choices:
        print("adding {} ".format( current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)


        # if current_choice == "1":
        #     computer_parts.append("Computer")
        # elif current_choice =="2":
        #     computer_parts.append("monitor")
        # elif current_choice == "3":
        #     computer_parts.append("mouse mat")
        # elif current_choice == "4":
        #     computer_parts.append("mouse")
        # elif current_choice == "5":
        #     computer_parts.append("keyboard")
        # elif current_choice == "6":
        #     computer_parts.append("hdmi")
    else:
        print("please select a valid option")
        # for part in available_parts:
        #     print("{0}: {1} ".format(available_parts.index(part) + 1 , part ))
        for number, part in enumerate(available_parts):
            print("{0}: {1} ".format(number + 1 , part ))
            #both the for loops perform the same function but one is efficient than the other
    current_choice = input()
print(computer_parts)