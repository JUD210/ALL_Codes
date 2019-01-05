# https://stackoverflow.com/questions/45849120/python-tuple-vs-generator


""" """
temp = (i for i in [1, 2, 3, 4])
gen = temp

# print(gen[0])
# TypeError: 'generator' object is not subscriptable

print(type(gen), gen, *gen, sep="\n")
# <class 'generator'>
# <generator object <genexpr> at 0x0000016842E792A0>
# 1
# 2
# 3
# 4


print(id((i for i in [1, 2, 3, 4])))
print(id(temp))
print(id(gen))
# 2564024210200
# 2564024210080
# 2564024210080


""" """
gen = (i for i in [1, 2, 3, 4])

tpl = tuple(gen)
print(tpl, *tpl, sep="\n")
# (1, 2, 3, 4)
# 1
# 2
# 3
# 4

tpl = tuple(gen)
print(tpl, *tpl, sep="\n")
# ()

""" SyntaxError: can't use starred expression here
gen = (i for i in [1, 2, 3, 4])

tpl = (*gen)
print(type(tpl), tpl, *tpl, sep="\n")
"""


""" """
gen = (i for i in [1, 2, 3, 4])

lst = list(gen)
print(lst, *lst, sep="\n")
# [1, 2, 3, 4]
# 1
# 2
# 3
# 4

lst = list(gen)
print(lst, *lst, sep="\n")
# []


gen = (i for i in [1, 2, 3, 4])

lst = [*gen]
print(lst, *lst, sep="\n")
# [1, 2, 3, 4]
# 1
# 2
# 3
# 4
