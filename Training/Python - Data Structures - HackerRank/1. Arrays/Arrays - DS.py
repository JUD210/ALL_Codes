# https://www.hackerrank.com/challenges/arrays-ds/problem


# Inputs
standard_input = """4
1 4 3 2"""


_, lst = input(), [int(s) for s in input().split()]
# 4
# 1 4 3 2

print(*lst[-1::-1])
# 2 3 4 1
