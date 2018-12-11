# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def decimal_to_binary(num):
    while True:
        try:
            num_bin = bin(int(num))[2:]
            break
        except:
            print("Please Enter Integer Only. (1 <= n <= 10^6)")

    return num_bin


def maximum_consecutive_1(num_bin):

    maximum_count = 0
    count = 0
    for c in num_bin:
        if c == "1":
            count += 1

            if count > maximum_count:
                maximum_count = count
        else:
            count = 0

    return maximum_count


if __name__ == "__main__":

    num_bin = decimal_to_binary(input())
    result = maximum_consecutive_1(num_bin)
    print(result)
