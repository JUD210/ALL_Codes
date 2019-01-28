# https://www.hackerrank.com/challenges/np-min-and-max/problem


# Inputs
standard_input = """4 2
2 5
3 7
1 3
4 0"""

# no [use-before-def]
m = None


import numpy


m, n = [int(s) for s in input().split()]
# 4 2

arr = numpy.array([input().split() for _ in range(m)], int)
# 2 5
# 3 7
# 1 3
# 4 0

result = numpy.min(arr, axis = 1)
# print(result)
# [2 3 1 0]

result = numpy.max(result)
print(result)
# 3


""" Reference

my_array = numpy.array([[2, 5], [3, 7], [1, 3], [4, 0]])

print(numpy.min(my_array, axis=0))
# [1 0]
print(numpy.min(my_array, axis=1))
# [2 3 1 0]
print(numpy.min(my_array, axis=None))
# 0
print(numpy.min(my_array))
# 0

print(numpy.max(my_array, axis=0))
# [4 7]
print(numpy.max(my_array, axis=1))
# [5 7 3 4]
print(numpy.max(my_array, axis=None))
# 7
print(numpy.max(my_array))
# 7

"""
