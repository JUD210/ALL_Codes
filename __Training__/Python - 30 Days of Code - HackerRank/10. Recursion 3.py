# https://www.hackerrank.com/challenges/30-recursion/problem


# Inputs
standard_input = """6"""


import math
import os
import random
import re
import sys

""" Complete the factorial function below. """


def input_num():
    while True:
        try:
            num = int(input())
            # 6
            if num <= 0:
                print("The number must be larger than 0")
                continue
            break

        except:
            print("Please Enter Integer Only!")

    return num


def factorial(n):
    if n != 1:
        return n * factorial(n - 1)
    else:
        return n


if __name__ == "__main__":
    num = input_num()
    result = factorial(num)
    print(result)
    # 720
