""" Good practice

It is best to define variables in the smallest scope they will be needed in. While functions can refer to variables defined in a larger scope, this is very rarely a good idea since you may not know what variables you have defined if your program has a lot of variables.
"""


""" Variable Scope

Variable scope refers to which parts of a program a variable can be referenced, or used, from.
"""


""" This will result in an error.

# def some_function():
#     word = "hello"
#
# print(word)


In the example above and the example below, word is said to have scope that is only local to each function.

"""
# This works fine.


def some_function():
    word = "hello"


def another_function():
    word = "goodbye"


"""
Here, word is said to have a global scope.
"""

# This works fine.

word = "hello"


def some_function():
    print(word)


some_function()

"""
Notice that we can still access the value of the global variable word within this function. 

However, the value of a global variable can not be modified inside the function.

If you want to modify that variable's value inside this function, it should be passed in as an argument.
"""

""" This will result in an error.

# word = "hello"

# def some_function():
#     print(word)
#     word = "TEST"

# some_function()

# UnboundLocalError: local variable 'word' referenced before assignment

# It is because Python doesn't allow functions to modify variables that aren't in the function's scope.
"""

word = "hello"


def some_function():

    word = "TEST"
    print(word)


some_function()


""" This will result in an error.

# def print_fn():
#     str1 = 'Variable scope is an important concept.'
#     print(str1)
# 
# print_fn(str1)

# NameError: name 'str1' is not defined
"""

""" This will result in an error.
"""
# str1 = 'Test'
#
# def print_fn():
#     str1 = 'Variable scope is an important concept.'
#     print(str1)
#
# print_fn(str1)

# TypeError: print_fn() takes 0 positional arguments but 1 was given

