coord = x, y, z = (1, 2, 3)
print(coord, "\n", x, y, z)
# (1, 2, 3)
#  1 2 3

coord = x, y, z = [1, 2, 3]
print(coord, "\n", x, y, z)
# [1, 2, 3]
#  1 2 3


coord = x, y, z = (1), (2), (3)
print(coord, "\n", x, y, z)
# (1, 2, 3)
#  1 2 3

coord = x, y, z = [1], [2], [3]
print(coord, "\n", x, y, z)
# ([1], [2], [3])
#  [1] [2] [3]

coord = x, y, z = (1,), (2,), (3,)
print(coord, "\n", x, y, z)
# ((1,), (2,), (3,))
#  (1,) (2,) (3,)


coord = x, y, z = map(int, "1 2 3".split())
print(coord, "\n", x, y, z)
# <map object at 0x000001B49201F2B0>
#  1 2 3

coord = x, y, z = [a for a in range(1, 4)]
print(coord, "\n", x, y, z)
# (1, 2, 3)
#  1 2 3
