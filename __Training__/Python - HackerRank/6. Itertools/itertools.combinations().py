# https://www.hackerrank.com/challenges/itertools-combinations/problem


from itertools import combinations

""" combinations(iterable, r)
returns the r length subsequences of elements from the input iterable.
: nCr = n! / (r! * (n-r)!) = nPr / r!


print(list(combinations("12345", 2)))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), 
# ('2', '3'), ('2', '4'), ('2', '5'), 
# ('3', '4'), ('3', '5'), 
# ('4', '5')]

A = [1, 1, 3, 3, 3]
print(list(combinations(A, 4)))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

"""

s, n = input().split()
# HACK 2

s = sorted(s)

# ["".join(chars) for i in range(1, int(n) + 1) for chars in combinations(s, i)]
# ['A', 'C', 'H', 'K', 'AC', 'AH', 'AK', 'CH', 'CK', 'HK']

print(
    *["".join(chars) for i in range(1, int(n) + 1) for chars in combinations(s, i)],
    sep="\n"
)
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
