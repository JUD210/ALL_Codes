# https://www.hackerrank.com/challenges/30-loops/problem

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

for i in range(1, 10 + 1):
    print("{} x {} = {}".format(n, i, n * i))

