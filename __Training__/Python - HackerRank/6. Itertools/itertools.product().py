# https://www.hackerrank.com/challenges/itertools-product/problem


from itertools import product

""" product(a, b)
computes the cartesian product of input iterables.


print(list(product([1, 2, 3], repeat=2)))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print(list(product([1, 2, 3], [10, 20])))
# [(1, 10), (1, 20),
# (2, 10), (2, 20),
# (3, 10), (3, 20)]

print(list(product([1, 2, 3], [10, 20], [100, 200])))
# [(1, 10, 100), (1, 10, 200), (1, 20, 100), (1, 20, 200),
# (2, 10, 100), (2, 10, 200), (2, 20, 100), (2, 20, 200),
# (3, 10, 100), (3, 10, 200), (3, 20, 100), (3, 20, 200)]

"""

a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 1 2
# 3 4

print(*product(a, b))
# (1, 3) (1, 4) (2, 3) (2, 4)
