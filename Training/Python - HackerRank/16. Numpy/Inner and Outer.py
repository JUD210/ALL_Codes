# https://www.hackerrank.com/challenges/np-inner-and-outer/problem


# Inputs
standard_input = """0 1
2 3"""


import numpy


a = numpy.array(input().split(), int)
# 0 1
b = numpy.array(input().split(), int)
# 2 3

print(numpy.inner(a, b))
# 3
print(numpy.outer(a, b))
# [[0 0]
#  [2 3]]


""" Reference 

a = numpy.array([0, 1])
b = numpy.array([3, 4])

print(numpy.inner(a, b))
# 4
print(numpy.outer(a, b))
# [[0 0]
#  [3 4]]

"""

