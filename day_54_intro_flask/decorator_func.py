import time as t


def decorator_function(function):
    def wrapper_function():
        t.sleep(2)
        function()

    return wrapper_function()


def bye():
    print('bye')


bye()


@decorator_function
def hello():
    print('hello')


def greetings():
    print("how r u")


delay_decorator = decorator_function(greetings)

delay_decorator()
