# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem


# Inputs
standard_input = """10
1000000000
1000000001
1000000002
1000000003
1000000004
1000000005
1000000006
1000000007
1000000008
1000000009"""

import math


def check_prime(num):

    if num < 2:
        return "Not prime"
    elif num == 2:
        return "Prime"

    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return "Not prime"

    return "Prime"


# 1 <= t <= 30
t = int(input())

for _ in range(t):
    # 10

    # 1 <= n <= 2e+9
    print(check_prime(int(input())))
    # 1000000000
    # 1000000001
    # 1000000002
    # 1000000003
    # 1000000004
    # 1000000005
    # 1000000006
    # 1000000007
    # 1000000008
    # 1000000009

# Not prime
# Not prime
# Not prime
# Not prime
# Not prime
# Not prime
# Not prime
# Prime
# Not prime
# Prime
