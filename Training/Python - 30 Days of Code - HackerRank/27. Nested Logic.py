# https://www.hackerrank.com/challenges/30-nested-logic/problem


# Inputs
standard_input = """9 6 2015
6 6 2015"""

# Such a unrealistic... 12 31 2018 , 1 1 2019 : 10000 hacko


# returned / expected
rd, rm, ry = [int(x) for x in input().split()]
ed, em, ey = [int(x) for x in input().split()]


if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
# 45
