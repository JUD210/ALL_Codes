# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem


import re

# Inputs
standard_input = """12
(7, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)"""


pair_pattern = re.compile(
    r"""
    ^\(
    [+-]? ((90(\.0+)?) | ([1-8]\d(\.\d+)?) | (\d(\.\d+)?)) # x part
    , # comma
    \  # whitespace
    [+-]? ((180(\.0+)?) | ((1[0-7]\d | [1-9]\d | \d)(\.\d+)?)) # y part
    \)$""",
    re.X,
)

for x in range(int(input())):
    if pair_pattern.match(input()):
        print("Valid")
    else:
        print("Invalid")

# Valid
# Valid
# Valid
# Valid
# Valid
# Valid
# Invalid
# Invalid
# Invalid
# Invalid
# Invalid
# Invalid
