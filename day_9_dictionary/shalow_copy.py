animals = {
    "tiger": "scary",
    "elephant": "scary big",
    "teddy": "cuddly",
}

things = animals.copy()
animals["teddy"] = "toy"
print(things["teddy"])
print(animals["teddy"])