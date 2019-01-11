# https://www.hackerrank.com/challenges/most-commons/problem


""" Solution """

from collections import Counter

[print(*c) for c in Counter(sorted(input())).most_common(3)]


""" My Answer """

d = dict()

s = sorted([c for c in input()])
# edccbbbaa

# to
# aabbbccde


for c in s:
    d[c] = d.get(c, 0) + 1

k = list(d.keys())
v = list(d.values())

for _ in range(3):
    index = v.index(max(v))
    print(k[index], v[index])

    k.pop(index)
    v.pop(index)
# b 3
# a 2
# c 2
