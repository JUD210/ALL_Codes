# https://www.hackerrank.com/challenges/30-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
numbers = input().split()

arr = numbers[::-1]
print(*arr)
# 4
# 5 3 2 1
# 1 2 3 5
