# https://www.hackerrank.com/challenges/30-2d-arrays/problem

import math
import os
import random
import re
import sys

is_debug_mode = True


arr = []

""" Automatic Input """
if is_debug_mode == True:
    arr.append(list(map(int, "1 1 1 0 0 0".split())))
    arr.append(list(map(int, "0 1 0 0 0 0".split())))
    arr.append(list(map(int, "1 1 1 0 0 0".split())))
    arr.append(list(map(int, "0 0 2 4 4 0".split())))
    arr.append(list(map(int, "0 0 0 2 0 0".split())))
    arr.append(list(map(int, "0 0 1 2 4 0".split())))

    for y in range(6):
        for x in range(6):
            sys.stdout.write(str(arr[y][x]) + " ")
        print("")

    # 1 1 1 0 0 0
    # 0 1 0 0 0 0
    # 1 1 1 0 0 0
    # 0 0 2 4 4 0
    # 0 0 0 2 0 0
    # 0 0 1 2 4 0

""" Manual Input """
if is_debug_mode == False:
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))


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
