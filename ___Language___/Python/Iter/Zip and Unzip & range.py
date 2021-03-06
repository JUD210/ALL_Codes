a = [1, 2, 3]
b = [4, 5]


r = ((x, y) for x in a for y in b)
print(r)
# <generator object <genexpr> at 0x00000182580A0B88>
print(*r)
# (1, 4) (1, 5) (2, 4) (2, 5) (3, 4) (3, 5)

r = [(x, y) for x in a for y in b]
print(r)
# [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
print(*r)
# (1, 4) (1, 5) (2, 4) (2, 5) (3, 4) (3, 5)
print(*r)
# Prints Nothing


l = []
l.append([1, 2, 3])
l.append([4, 5])

print(*zip(*l))
# (1, 4) (2, 5)


print(*zip((1, 2, 3), (10, 20, 30), (100, 200, 300)), sep="\n")
# (1, 10, 100)
# (2, 20, 200)
# (3, 30, 300)

print(*zip((1,), (10, 20), (100, 200, 300)), sep="\n")
# (1, 10, 100)

print(*[(1, 2, 3), (10, 20, 30), (100, 200, 300)], sep="\n")
# (1, 2, 3)
# (10, 20, 30)
# (100, 200, 300)

print([*range(1, 4)], [*range(10, 40, 10)], *range(100, 400, 100), sep="\n")
# [1, 2, 3]
# [10, 20, 30]
# 100
# 200
# 300
