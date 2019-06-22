# https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-1-9mpr98pgr


def add_all_arguments(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_all_arguments(1, 5, 7, 9, 10))  # 32
print(add_all_arguments(1, 9))  # 10
print(add_all_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
print(add_all_arguments(1))  # 1
print(add_all_arguments())  # 0


def print_arguments(**kwargs):
    print(kwargs)


print_arguments(name="Moyosore")
# {'name': 'moyosore'}
print_arguments(name="Moyosore", country="Nigeria")
# {'name': 'moyosore', 'country': 'Nigeria'}
print_arguments()
# {}


def print_argument_values(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_argument_values(name="Moyosore", country="Nigeria")
# name: Moyosore
# country: Nigeria


"""
Args and kwargs can be used together in a function, with args always coming before kwargs. If there are any other required arguments, they come before args and kwargs

"""


def add_and_mul1(*args, **kwargs):
    pass


def add_and_mul2(my_arg, *args, **kwargs):
    pass


def add_and_mul3(my_arg, my_arg_1, *args, **kwargs):
    pass

