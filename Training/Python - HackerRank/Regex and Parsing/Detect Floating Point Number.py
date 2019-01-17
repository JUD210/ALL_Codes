# https://www.hackerrank.com/challenges/introduction-to-regex/problem


import re


# Number can start with +, - or . symbol.
# Number must have exactly one . symbol.
# Number must contain at least 1 decimal value.
# Number must not give any exceptions when converted using float(N).

""" Solution """
for _ in range(int(input())):
    # 8
    num = input()
    # +4.50
    # -1.0
    # .5
    # -.7
    # +.4
    # 12.
    # -+4.5
    # HELLO, World!

    print(bool(re.match(r"^[-+]?\d*\.\d+$", num)))
    # True
    # True
    # True
    # True
    # True
    # False
    # False
    # False

# ^[-+]?[0-9]*\.[0-9]+$

""" My Answer """


def detector(s):
    try:
        if len(s.split(".")) != 2:
            return False
        s = float(s)
        return True
    except:
        return False


for _ in range(int(input())):
    # 8

    s = input()
    # +4.50
    # -1.0
    # .5
    # -.7
    # +.4
    # 12.
    # -+4.5
    # HELLO, World!

    print(detector(s))
    # True
    # True
    # True
    # True
    # True
    # False
    # False
    # False
