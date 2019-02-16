"""
The single * means that there can be any number of extra positional arguments. foo() can be invoked like foo(1,2,3,4,5). In the body of foo() param2 is a sequence containing 2-5.

The double ** means there can be any number of extra named parameters. bar() can be invoked like bar(1, a=2, b=3). In the body of bar() param2 is a dictionary containing {'a':2, 'b':3 }

"""


def foo(param1, *param2):
    print(param1)
    print(param2)


foo(1, 2, 3, 4, 5)
# 1
# (2, 3, 4, 5)


def bar(param1, **param2):
    print(param1)
    print(param2)


bar(1, a=2, b=3)
# 1
# {'a': 2, 'b': 3}


def foo2(x, y, z):
    print("x=" + str(x))
    print("y=" + str(y))
    print("z=" + str(z))


mylist = [1, 2, 3]
foo2(*mylist)
# x=1
# y=2
# z=3

mydict = {"x": 1, "y": 2, "z": 3}
foo2(*mydict)
# x=x
# y=y
# z=z

foo2(**mydict)
# x=1
# y=2
# z=3

mytuple = (1, 2, 3)
foo2(*mytuple)
# x=1
# y=2
# z=3
