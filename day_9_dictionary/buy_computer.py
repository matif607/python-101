available_parts = {
    '1': 'computer',
    '2': 'monitor',
    '3': 'keyboard',
    '4': 'mouse',
    '5': 'hdmi cable',
    '6': 'dvd drive'
}

# computer_parts = []
computer_parts = {}

current_choice = None
while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f" {chosen_part} already in the list, removing {chosen_part} from dictionary")
            computer_parts.pop(current_choice)
        else:
            print(f"adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
    else:
        for key, value in available_parts.items():
            # print(key, value, sep=': ')
            print(f"{key}: {value}")
        print("0 to finish")
    current_choice = input(':>')

print(computer_parts)
