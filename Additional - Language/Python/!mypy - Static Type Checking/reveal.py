# https://realpython.com/python-type-checking/


import math


# reveal_type(math.pi)
# [mypy] Revealed type is 'builtins.float' [error]


radius = 1
circumference = 2 * math.pi * radius
# reveal_locals()
# [mypy] Revealed local types are: [error]
# [mypy] circumference: builtins.float [error]
# [mypy] radius: builtins.int [error]

"""
Note: The reveal expressions are only meant as a tool helping you add types and debug your type hints. If you try to run the reveal.py file as a Python script it will crash with a NameError since reveal_type() is not a function known to the Python interpreter.

"""
