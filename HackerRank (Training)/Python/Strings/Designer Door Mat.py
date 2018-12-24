# https://www.hackerrank.com/challenges/designer-door-mat/problem5


height, width = tuple(map(int, input().split()))
# 7 21

pattern = ".|."

# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------


for i in range(height // 2, -(height // 2) - 1, -1):
    # i       3 2 1 0-1-2-3
    # pattern 1 3 5 w 5 3 1

    if i == 0:
        print("WELCOME".center(width, "-"))
    else:
        print((pattern * (height - (abs(i) * 2))).center(width, "-"))
