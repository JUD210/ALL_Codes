# https://www.hackerrank.com/challenges/incorrect-regex/problem


import re

for _ in range(int(input())):
    # 2
    try:
        regex = re.compile(input())
        # .*\+
        # .*+

        print("True")
    except re.error:
        print("False")

# True
# False
