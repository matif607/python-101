from contents import recipes, pantry


def item_to_buy(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to `data` dictionary"""
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}

for index, key in enumerate(recipes):
    # print(index + 1, key)
    display_dict[str(index + 1)] = key

shopping_list = {}
while True:
    print("please chose your recipe")
    print('-' * 80)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(': ')

    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"you have selected {selected_item}")
        ingredients = recipes[selected_item]
        print(ingredients)
        print("checking item in pantry...")
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print("\t OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\t you need to buy {quantity_to_buy} of {food_item}")
                item_to_buy(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)
