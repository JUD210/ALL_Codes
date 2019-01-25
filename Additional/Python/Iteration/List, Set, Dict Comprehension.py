# no-use-before-def
x = None
y = None
z = None
n = None


""" List Comprehension """

squares = {x ** 2 for x in range(9)}
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64]

squares = {x ** 2 for x in range(9) if x % 2 == 0}
print(squares)
# [0, 4, 16, 36, 64]

squares = {x ** 2 if x % 2 == 0 else x + 3 for x in range(9)}
print(squares)
# [0, 4, 4, 6, 16, 8, 36, 10, 64]

# A if B else C:
# if B is True, insert A
# if B is False, insert C


x, y, z, n = 1, 1, 1, 2
lst = [
    (i, j, k, i + j + k)
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
]

print(type(lst), lst, *lst, sep="\n")
# <class 'list'>
# [(0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1), (1, 0, 0, 1), (1, 1, 1, 3)]
# (0, 0, 0, 0)
# (0, 0, 1, 1)
# (0, 1, 0, 1)
# (1, 0, 0, 1)
# (1, 1, 1, 3)


""" Set Comprehension """


squares = {x ** 2 for x in range(9)}
print(squares)
# {0, 1, 64, 4, 36, 9, 16, 49, 25}

squares = {x ** 2 for x in range(9) if x % 2 == 0}
print(squares)
# {0, 64, 4, 36, 16}

squares = {x ** 2 if x % 2 == 0 else x + 3 for x in range(9)}
print(squares)
# {0, 64, 4, 36, 6, 8, 10, 16}

# A if B else C:
# if B is True, insert A
# if B is False, insert C


x, y, z, n = 1, 1, 1, 2
lst = {
    (i, j, k, i + j + k)
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
}

print(type(lst), lst, *lst, sep="\n")
# <class 'set'>
# {(1, 0, 0, 1), (0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 1, 3)}
# (1, 0, 0, 1)
# (0, 0, 0, 0)
# (0, 1, 0, 1)
# (0, 0, 1, 1)
# (1, 1, 1, 3)


""" Dictionary Comprehension """


squares = {i: x ** 2 for i, x in enumerate(range(9))}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

squares = {i: x ** 2 for i, x in enumerate(range(9)) if x % 2 == 0}
print(squares)
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

squares = {i: x ** 2 if x % 2 == 0 else x + 3 for i, x in enumerate(range(9))}
print(squares)
# {0: 0, 1: 4, 2: 4, 3: 6, 4: 16, 5: 8, 6: 36, 7: 10, 8: 64}

# A if B else C:
# if B is True, insert A
# if B is False, insert C


x, y, z, n = 1, 1, 1, 2
lst = {
    (i, j, k): i + j + k
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
}

print(type(lst), lst, *lst.items(), sep="\n")
# <class 'dict'>
# {(0, 0, 0): 0, (0, 0, 1): 1, (0, 1, 0): 1, (1, 0, 0): 1, (1, 1, 1): 3}
# ((0, 0, 0), 0)
# ((0, 0, 1), 1)
# ((0, 1, 0), 1)
# ((1, 0, 0), 1)
# ((1, 1, 1), 3)
