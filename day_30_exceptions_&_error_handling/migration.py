import ducks

flocks = ducks.Flock()

donald = ducks.Duck()
daisy = ducks.Duck()
sana = ducks.Duck()
atif = ducks.Duck()
anas = ducks.Duck()
saad = ducks.Duck()
maaz = ducks.Duck()
percy = ducks.Penguin()

flocks.add_duck(donald)
flocks.add_duck(daisy)
flocks.add_duck(atif)
flocks.add_duck(anas)
flocks.add_duck(percy)
flocks.add_duck(sana)
flocks.add_duck(saad)
flocks.add_duck(maaz)

flocks.migrate()



