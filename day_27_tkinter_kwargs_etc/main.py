import tkinter

window = tkinter.Tk()


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 5, 5))


def calculate(n, **kwargs):
    print((type(kwargs)))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


some_value = calculate(2, add=3, multiply=5)
print(some_value)


class Car:

    def __int__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")  # in kw instead of getting it from dictionary we can use .get


my_car = Car()

print(my_car.model)
