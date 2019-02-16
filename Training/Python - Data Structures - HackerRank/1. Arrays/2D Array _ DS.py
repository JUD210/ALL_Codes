# https://www.hackerrank.com/challenges/2d-array/problem


# Inputs
standard_input = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""


lst = []
for _ in range(6):
    lst.append([int(s) for s in input().split()])

# print(*lst, sep="\n")
# [1, 1, 1, 0, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [1, 1, 1, 0, 0, 0]
# [0, 0, 2, 4, 4, 0]
# [0, 0, 0, 2, 0, 0]
# [0, 0, 1, 2, 4, 0]


hourglass_sum = []
for y in range(4):
    for x in range(4):
        hourglass_sum.append(
            sum([sum(ly[x : x + 3]) for ly in lst[y : y + 3]])
            - lst[y + 1][x]
            - lst[y + 1][x + 2]
        )

# print(hourglass_sum)
# [7, 4, 2, 0, 4, 8, 10, 8, 3, 6, 7, 6, 3, 9, 19, 14]

print(max(hourglass_sum))
# 19
