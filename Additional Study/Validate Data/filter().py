print(list(filter(None, [False, False, True, True])))
# [True, True]

print(list(filter(None, [0, 0, 1, 1, 2, 2, 3, 3])))
# [1, 1, 2, 2, 3, 3]

print(list(filter(lambda n: n > 1, [0, 0, 1, 1, 2, 2, 3, 3])))
# [2, 2, 3, 3]

d = dict()
d = {"c": 3, "b": 2, "a": 2}
print(list(filter(lambda t: t[1] == max(d.values()), d.items()))[0][0])
# c