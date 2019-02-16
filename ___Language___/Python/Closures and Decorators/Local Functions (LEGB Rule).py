# https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-1-9mpr98pgr


# LEGB Rule : - Local, Eclosing, Global, Built-in

x = "global"


def outer_func():
    y = "enclose"

    def inner_func():
        z = "local"
        print(x, y, z)
        return "I'm in inner_func()"

    return inner_func()


print(outer_func())
# global enclose local
# I'm in inner_func()
