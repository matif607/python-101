class Book:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

b1 = Book("honeycomb", 100)
# b1.book = 100
# print(b1.name)
# print(b1.price)

def printBook(self):
    print(f"name: {self.name}")
    print(f"price: {self.price}")

b3 = Book("honeycomb", 100)
b4 = Book("invisible man", 500)

b3.Book()
b4.Book()
