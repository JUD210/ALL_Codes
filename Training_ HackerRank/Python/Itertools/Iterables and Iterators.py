# https://www.hackerrank.com/challenges/iterables-and-iterators/problem


from itertools import combinations

n, s, select = int(input()), input().split(), int(input())
# 4
# a a c d
# 2

l_comb = list(combinations(s, select))
l_comb_filtered = list(filter(lambda c: "a" in c, l_comb))
# print(l_comb)
# [('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')]
# print(l_comb_filtered)
# [('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd')]

probability = len(l_comb_filtered) / len(l_comb)
print("{:.3f}".format(probability))
# 0.833
