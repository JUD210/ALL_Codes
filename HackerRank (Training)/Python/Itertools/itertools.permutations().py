# https://www.hackerrank.com/challenges/itertools-permutations/problem


from itertools import permutations

""" permutations(iterable[, r]) 
returns successive r length permutations of elements in an iterable.


print(list(permutations([1, 2, 3])))
# [(1, 2, 3), (1, 3, 2), 
# (2, 1, 3), (2, 3, 1), 
# (3, 1, 2), (3, 2, 1)]

print(list(permutations([1, 2, 3, 4], 2)))
# [(1, 2), (1, 3), (1, 4), 
# (2, 1), (2, 3), (2, 4), 
# (3, 1), (3, 2), (3, 4), 
# (4, 1), (4, 2), (4, 3)]

print(list(permutations("abc", 3)))
# [('a', 'b', 'c'), ('a', 'c', 'b'), 
# ('b', 'a', 'c'), ('b', 'c', 'a'), 
# ('c', 'a', 'b'), ('c', 'b', 'a')]

"""

s, n = input().split()
# HACK 2


""" Refence

for chars in permutations(sorted(s), r=int(n)):
    print(chars)
    # ('A', 'C')

    # c = *chars
    # SyntaxError: can't use starred expression here

    print(*chars)
    # A C

    print(*chars, sep="")
    # AC

    c = "".join(chars)
    print(c)
    # AC

    print("".join(chars))
    # AC
"""

l = ["".join(chars) for chars in permutations(sorted(s), int(n))]
# ['AC', 'AH', 'AK', 'CA', 'CH', 'CK', 'HA', 'HC', 'HK', 'KA', 'KC', 'KH']

print(*l, sep="\n")
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HA
# HC
# HK
# KA
# KC
# KH
