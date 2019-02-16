# https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-1-9mpr98pgr


""" Why use decorators

They are powerful and widely used in python
They improve code clarity
They reduce code complexity

"""


def outer(f):
    print("I'm in outer!")

    def inner():
        print("I'm in inner!")
        return f().upper()

    return inner


def introducer1():
    return "let's introduce decorator"


print(outer(introducer1)())
# I'm in outer!
# I'm in inner!
# LET'S INTRODUCE DECORATOR


@outer
def introducer2():
    return "let's introduce decorator"


print(introducer2())
# I'm in outer!
# I'm in inner!
# LET'S INTRODUCE DECORATOR


######################################
# A decorator is a callable function


def capitalize(func):
    def uppercase():
        return func().upper()

    return uppercase


def silent_hello(name="Hyeogikarp"):
    return "hello " + name


@capitalize
def loud_hello(name="Hyeogikarp"):
    return "hello " + name


print(silent_hello())
# hello hyeogikarp

print(loud_hello())
# HELLO HYEOGIKARP


print(silent_hello)
# <function silent_hello at 0x0000024F31F23488>


print(loud_hello)
# <function capitalize.<locals>.uppercase at 0x000001DBFD763598>
print(capitalize(loud_hello))
# <function capitalize.<locals>.uppercase at 0x000002CAEF6C3620>


print(capitalize(loud_hello)())
# HELLO HYEOGIKARP


######################################


def square_origin(func):
    print("in square_origin")

    def multiply(*args):
        print("in multiply")
        print(f"args: {args} -> func(*args): {func(*args)}")
        return func(*args) * func(*args)

    print("out square_origin")

    return multiply


def addition_xy_origin1(x, y):
    print("in addition_xy_origin1")
    return x + y


print(square_origin(addition_xy_origin1)(5, 7))
# in square_origin
# out square_origin
# in multiply
# in addition_xy_origin
# args: (5, 7) -> func(*args): 12
# in addition_xy_origin
# in addition_xy_origin
# 144


@square_origin
def addition_xy_origin2(x, y):
    print("in addition_xy_origin1")
    return x + y


print(addition_xy_origin2(5, 7))
# in square_origin
# out square_origin
# in multiply
# in addition_xy_origin1
# args: (5, 7) -> func(*args): 12
# in addition_xy_origin1
# in addition_xy_origin1
# 144


######################################
""" Below is minor detail I couldn't understand... """


def square(func):
    print("in square")

    def multiply(*args):
        print("in multiply")
        print(f"args: {args} -> func(*args): {func(*args)}")
        return func(*args) * func(*args)

    print("out square")

    return multiply


@square
def addition_xy(x, y):
    print("in addition_xy")
    return x + y


@square
def test():
    pass


# in square
# out square
# in square
# out square


print(addition_xy(5, 7))
# in multiply
# in addition_xy
# 144

print(addition_xy(15, 10))
# in multiply
# in addition_xy
# 625


""" Can't understand why... """
print(square(addition_xy)(5, 7))
# in square
# out square
# in multiply
# in multiply
# in addition_xy
# args: (5, 7) -> func(*args): 12
# in addition_xy
# in addition_xy
# args: (5, 7) -> func(*args): 144
# in multiply
# in addition_xy
# args: (5, 7) -> func(*args): 12
# in addition_xy
# in addition_xy
# in multiply
# in addition_xy
# args: (5, 7) -> func(*args): 12
# in addition_xy
# in addition_xy
# 20736
