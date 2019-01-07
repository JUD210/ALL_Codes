arr1 = list(map(int, input().split()))
arr2 = [*map(int, input().split())]
# 1 2 3
# 1 2 3

print(arr1)
print(arr2)
# [1, 2, 3]
# [1, 2, 3]

print(
    *map(
        lambda n1, n10, n100: n1 + n10 + n100,
        *[(1, 2, 3), (10, 20, 30), (100, 200, 300)]
    ),
    sep="\n"
)
# 111
# 222
# 333

print(
    *map(lambda n1, n10, n100: n1 + n10 + n100, *[(1,), (10, 20), (100, 200, 300)]),
    sep="\n"
)
# 111

print(*map(lambda a, b, c: a * 1 + b * 3 + c * 5, *"ABC"))
# ABBBCCCCC


""" TypeError: 'int' object is not iterable

print(
    *map(lambda n1, n10, n100: n1 + n10 + n100, *[(1), (10, 20), (100, 200, 300)]),
    sep="\n"
)

print(type((1)))
# <class 'int'>

print(type((1,)))
# <class 'tuple'>
"""
