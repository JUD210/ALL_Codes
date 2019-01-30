# https://realpython.com/python-type-checking/


"""

import math


reveal_type(math.pi)
# [mypy] Revealed type is 'builtins.float' [error]


radius = 1
circumference = 2 * math.pi * radius

reveal_locals()
# [mypy] Revealed local types are: [error]
# [mypy] circumference: builtins.float [error]
# [mypy] radius: builtins.int [error]

"""
