current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in "123456":
        print("adding {} ".format( current_choice))
        if current_choice == "1":
            computer_parts.append("Computer")
        elif current_choice =="2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("mouse mat")
        elif current_choice == "4":
            computer_parts.append("monitor")
        elif current_choice == "5":
            computer_parts.append("monitor")
        elif current_choice == "6":
            computer_parts.append("hdmi")
    else:
        print("please select a valid option")
        print("1: Computer")
        print("2: monitor")
        print("3: mouse mat")
        print("4: cpu")
        print("5: monitor")
        print("6: hdmi")
        print("0: to finish")
    current_choice = input()
print(computer_parts)