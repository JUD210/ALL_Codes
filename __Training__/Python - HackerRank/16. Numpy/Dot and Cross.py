# https://www.hackerrank.com/challenges/np-dot-and-cross/problem


import numpy


# Inputs
standard_input = """2
1 2
3 4
1 2
3 4"""


num = int(input())

a = numpy.array([input().split() for _ in range(num)], int)
# 1 2
# 3 4
b = numpy.array([input().split() for _ in range(num)], int)
# 1 2
# 3 4

print(numpy.dot(a, b))
# [[ 7 10]
#  [15 22]]


""" Reference

a = numpy.array([1, 2])
b = numpy.array([3, 4])

print(numpy.dot(a, b))
# 11
print(numpy.cross(a, b))
# -2

"""
