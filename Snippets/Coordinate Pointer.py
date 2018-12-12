import math
import os
import random
import re
import sys


arr = []

arr.append(list(map(int, "1 1 1 0 0 0".split())))
arr.append(list(map(int, "0 1 0 0 0 0".split())))
arr.append(list(map(int, "1 1 1 0 0 0".split())))
arr.append(list(map(int, "0 0 2 4 4 0".split())))
arr.append(list(map(int, "0 0 0 2 0 0".split())))
arr.append(list(map(int, "0 0 1 2 4 0".split())))


def coordinate_pointer(arr, x, y):

    for ty in range(6):  # temp y
        for tx in range(6):
            if ty == y and tx == x:
                sys.stdout.write("C" + " ")
            else:
                sys.stdout.write(str(arr[ty][tx]) + " ")
        print("")

    return 0


if __name__ == "__main__":
    coordinate_pointer(arr, 4, 1)

