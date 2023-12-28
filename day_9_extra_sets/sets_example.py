farm_animals = {'hen', 'goat', 'horse', 'cow', 'sheep'}
print(farm_animals)
# sets are unordered

for animal in farm_animals:
    print(animal)

checking_sets = {'horse', 'hen', 'goat', 'sheep', 'cow'}

if farm_animals == checking_sets:
    print("the sets are equal")
else:
    print("sets are unequal")
# order is not necessary in sets as it is in list or tuple. Python considers it equal if it has the same values

