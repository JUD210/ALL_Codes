# https://www.hackerrank.com/challenges/triangle-quest-2/problem


# Condition

# 1 <= int(input()) <= 9
# String is not allowed.
# More than 1 for-statement is not allowed.
# More than 2 lines are not allowed. (Do not leave a blank line also.)

for i in range(1, int(input()) + 1):
    print(((10 ** i - 1) // 9) ** 2)
# 5

# 1
# 121
# 12321
# 1234321
# 123454321

# 1 * 1 = 1
# 11 * 11 = 121
# 111 * 111 = 12321
# ...