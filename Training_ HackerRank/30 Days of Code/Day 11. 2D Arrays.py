# https://www.hackerrank.com/challenges/30-2d-arrays/problem


import math
import os
import random
import re
import sys


arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0


def sum_hourglass(arr, x, y):
    result = 0
    blank = [(x, y + 1), (x + 2, y + 1)]

    for ty in range(y, y + 3):
        for tx in range(x, x + 3):
            if (tx, ty) not in blank:
                result += arr[ty][tx]

    return result


sum_results = []
for y in range(len(arr) - 2):
    for x in range(len(arr[y]) - 2):
        sum_results.append(sum_hourglass(arr, x, y))

print(max(sum_results))
# 19

# Reference
# 
# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0
# 
# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0
# 
# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0
# 
# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0