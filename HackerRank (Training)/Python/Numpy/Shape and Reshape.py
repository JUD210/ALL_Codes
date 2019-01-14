# https://www.hackerrank.com/challenges/np-shape-reshape/problem


import numpy

arr = numpy.array([int(s) for s in input().split()])
# 1 2 3 4 5 6 7 8 9

print(numpy.reshape(arr, (3, 3)))
# arr.shape = (3, 3)
# print(arr)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


""" Reference """
a = numpy.array([1, 2, 3, 4, 5, 6])
print(a)
# [1 2 3 4 5 6]

a.shape = (6, 1)
print(a)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

a.shape = (3, 2)
print(a)
# [[1 2]
#  [3 4]
#  [5 6]]


print(numpy.reshape(a, (1, 6)))
# [[1 2 3 4 5 6]]

print(a)
# [[1 2]
#  [3 4]
#  [5 6]]
