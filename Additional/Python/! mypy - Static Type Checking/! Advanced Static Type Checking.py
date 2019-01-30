# https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b


# If you are not using PyCharm, install mypy linter
# If you are using VS Code, Enable mypy in Settings


from typing import List, Tuple


# Inputs
standard_input = """test"""

points: List[Tuple[float, float]] = [
    (25.91375, -60.15503),
    (-11.01983, -166.48477),
    (-11.01983, -166.48477),
]


print(points)
# [(25.91375, -60.15503), (-11.01983, -166.48477), (-11.01983, -166.48477)]
