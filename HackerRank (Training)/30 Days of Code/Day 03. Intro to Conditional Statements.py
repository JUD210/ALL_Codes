# https://www.hackerrank.com/challenges/30-conditional-statements/problem


import math
import os
import random
import re
import sys


def evaluate(n):
    answer = None

    if n % 2 == 1:
        answer = "Weird"
    elif 2 <= n <= 5:
        answer = "Not Weird"
    elif 6 <= n <= 20:
        answer = "Weird"
    elif n > 20:
        answer = "Not Weird"

    return answer


test_n = print(evaluate(int(input())))
# 5
# Weird