coord1 = x, y, z = (1, 2, 3)
print(coord1, "\n", x, y, z)
# (1, 2, 3)
#  1 2 3

coord2 = x, y, z = [1, 2, 3]
print(coord2, "\n", x, y, z)
# [1, 2, 3]
#  1 2 3


coord3 = x, y, z = (1), (2), (3)
print(coord3, "\n", x, y, z)
# (1, 2, 3)
#  1 2 3

coord4 = x, y, z = [1], [2], [3]  # type: ignore
print(coord4, "\n", x, y, z)
# ([1], [2], [3])
#  [1] [2] [3]

coord5 = x, y, z = (1,), (2,), (3,)  # type: ignore
print(coord5, "\n", x, y, z)
# ((1,), (2,), (3,))
#  (1,) (2,) (3,)


coord6 = x, y, z = map(int, "1 2 3".split())
print(coord6, "\n", x, y, z)
# <map object at 0x000001B49201F2B0>
#  1 2 3

coord7 = x, y, z = [a for a in range(1, 4)]
print(coord7, "\n", x, y, z)
# (1, 2, 3)
#  1 2 3
