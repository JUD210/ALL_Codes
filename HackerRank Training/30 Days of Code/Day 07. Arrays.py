# https://www.hackerrank.com/challenges/30-arrays/problem


import math
import os
import random
import re
import sys

n = int(input())
# 4
numbers = input().split()
# 5 3 2 1

arr = numbers[::-1]
print(*arr)
# 1 2 3 5
