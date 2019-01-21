# https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-1-9mpr98pgr


# LEGB Rule : - Local, Eclosing, Global, Built-in


def outer(x):
    def inner(y=2):
        return x ** y

    return inner


print(outer(5)())  # 25
print(outer(5)(3))  # 125


##############################


def multiply_by(num):
    def multiply_by_num(k):
        return num * k

    return multiply_by_num


five = multiply_by(5)
print(five(2))  # 10
print(five(4))  # 20

decimal = multiply_by(10)
print(decimal(20))  # 200
print(decimal(3))  # 30


##############################

text = "global text"


def outer_func():
    text = "enclosing text"

    def inner_func1():
        text = "local text"
        print("inner_func1:", text)
        # inner_func1: local text

    def inner_func2():
        nonlocal text  # binds the local text to the enclosing text
        text = "EDITED ENCLOSING TEXT"
        print("inner_func2:", text)
        # inner_func2: EDITED ENCLOSING TEXT

    def inner_func3():
        global text  # binds the global text to the local text
        text = "EDITED GLOBAL TEXT"
        print("inner_func3:", text)
        # inner_func3 EDITED GLOBAL TEXT

    print("outer_func:", text)
    # outer_func: enclosing text
    inner_func1()
    inner_func2()
    inner_func3()
    print("outer_func:", text)
    # outer_func: EDITED ENCLOSING TEXT


print("global:", text)
# global: global text
outer_func()
print("global:", text)
# global: EDITED GLOBAL TEXT

""" Result

global: global text
outer_func: enclosing text
inner_func1: local text
inner_func2: EDITED ENCLOSING TEXT
inner_func3: EDITED GLOBAL TEXT
outer_func: EDITED ENCLOSING TEXT
global: EDITED GLOBAL TEXT

"""
