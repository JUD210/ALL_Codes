# https://www.hackerrank.com/challenges/list-comprehensions/problem


# Condition
# 1. lexicographic increasing order.
# 2. i+j+k != n


x = int(input())
y = int(input())
z = int(input())
n = int(input())
# 1
# 1
# 1
# 2

test0 = list(
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
)

test1 = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                test1.append([i, j, k])

test2 = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
]


test3 = (
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if (i + j + k != n)
)

# print(
#     type(test0),
#     test0,
#     "",
#     type(test1),
#     test1,
#     "",
#     type(test2),
#     test2,
#     "",
#     type(test3),
#     test3,
#     sep="\n",
# )

# <class 'list'>
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# <class 'list'>
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# <class 'list'>
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# <class 'generator'>
# <generator object <genexpr> at 0x000001BDC7351ED0>


print(test0)