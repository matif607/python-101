data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camelia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrun",
    "Peony - Shrub",
    "Red Hot Poker - Flower",
    "snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Watch Hazel - Shrub"
]

plants_filename = "flowers_write.txt"

# with open(plants_filename, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# new_plants = []
# with open(plants_filename, "r") as plants:
#     for plant in plants:
#         new_plants.append(plant.rstrip())
#
# print(new_plants)

with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)
