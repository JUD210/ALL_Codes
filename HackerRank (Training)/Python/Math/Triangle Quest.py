# https://www.hackerrank.com/challenges/python-quest-1/problem


# Condition

# 1 <= int(input()) <= 9
# String is not allowed.
# More than 1 for-statement is not allowed.
# More than 2 lines are not allowed. (Do not leave a blank line also.)


""" Mathmatical Answer

for i in range(1, int(input())):
    print(10**i // 9 * i)
"""

""" Cheating Answer

for i in range(1, int(input())):
    print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])
"""

for i in range(1, int(input())):
    print(sum(map(lambda num: i * 10 ** num, range(i))))

# 5

# 1
# 22
# 333
# 4444

""" Note

for i in range(1, int(input())):
    print(*map(lambda num: i * 10 ** num, range(i)))

# 5
# 1
# 2 20
# 3 30 300
# 4 40 400 4000
"""
