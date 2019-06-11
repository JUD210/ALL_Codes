# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem


from itertools import combinations_with_replacement

""" combinations_with_replacement(iterable, r)
returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.


print(list(combinations_with_replacement("12345", 2)))
# [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'),
# ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'),
# ('3', '3'), ('3', '4'), ('3', '5'),
# ('4', '4'), ('4', '5'),
# ('5', '5')]

"""

s, n = input().split()
# HACK 2

s = sorted(s)

print(*["".join(chars) for chars in combinations_with_replacement(s, int(n))], sep="\n")
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK
