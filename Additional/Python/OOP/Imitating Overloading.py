# Python Don't support Overloading!


""" Manual """


class Student:
    def hello(self, name=None):
        if name is not None:
            print("Hey " + name)
        else:
            print("Hey ")


std = Student()

std.hello()
# Hey

std.hello("Nicholas")
# Hey Nicholas


""" Using Single Dispatch """

from functools import singledispatch
from decimal import Decimal


@singledispatch
def add(a, b):
    raise NotImplementedError("Unsupported type")


@add.register(int)
@add.register(str)
@add.register(list)
@add.register(float)
@add.register(Decimal)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


add(1, 2)
# First argument is of type  <class 'int'>
# 3
add("Python", "Programming")
# First argument is of type  <class 'str'>
# PythonProgramming
add([1, 2, 3], [5, 6, 7])
# First argument is of type  <class 'list'>
# [1, 2, 3, 5, 6, 7]
add(1.23, 5.5)
# First argument is of type  <class 'float'>
# 6.73
add(Decimal(100.5), Decimal(10.789))
# First argument is of type  <class 'decimal.Decimal'>
# 111.2889999999999997015720510

# add((2,3), (3,4))
# NotImplementedError: Unsupported type


print(add.registry.keys())
# dict_keys([<class 'object'>, <class 'int'>, <class 'str'>, <class 'list'>, <class 'decimal.Decimal'>, <class 'float'>])
