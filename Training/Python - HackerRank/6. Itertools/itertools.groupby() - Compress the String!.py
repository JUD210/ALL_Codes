# https://www.hackerrank.com/challenges/compress-the-string/problem


from itertools import groupby

"""
print(*[(key, list(group)) for key, group in groupby("AAAABCCCDD")], sep="\n")
# ('A', ['A', 'A', 'A', 'A'])
# ('B', ['B'])
# ('C', ['C', 'C', 'C'])
# ('D', ['D', 'D'])

# type(group) : <class itertools._grouper>

"""

s = input()
# 1222311

print(*[(len(list(group)), int(key)) for key, group in groupby(s)])
# (1, 1) (3, 2) (1, 3) (2, 1)
