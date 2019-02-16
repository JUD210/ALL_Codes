# https://realpython.com/python-type-checking/


""" Dynamic Typing """


if False:
    1 + "two"  # This line never runs, so no TypeError is raised
else:
    1 + 2

# 1 + "two"
# Now this is type checked, and a TypeError is raised


""" Static Typing """


x: int = 5
x = "test"  # type: ignore
# [mypy] Incompatible types in assignment (expression has type "str", variable has type "int")  [error]


""" Duck Typing """
# You can call len() on any Python object that defines a .__len__() method:


class TheHobbit:
    def __len__(self):
        return 95022


the_hobbit = TheHobbit()
print(len(the_hobbit))
# 95022


# Note that the call to len() gives the return value of the .__len__() method. In fact, the implementation of len() is essentially equivalent to the following:
def len(obj):
    return obj.__len__()
