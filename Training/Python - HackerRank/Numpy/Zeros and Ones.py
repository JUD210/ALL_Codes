# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem


# Inputs
standard_input = """3 2 2 5"""


import numpy


shape = [int(s) for s in input().split()]
# 3 2 2 5

print(numpy.zeros(shape, numpy.int))
# [[[[0 0 0 0 0]
#    [0 0 0 0 0]]

#   [[0 0 0 0 0]
#    [0 0 0 0 0]]]


#  [[[0 0 0 0 0]
#    [0 0 0 0 0]]

#   [[0 0 0 0 0]
#    [0 0 0 0 0]]]


#  [[[0 0 0 0 0]
#    [0 0 0 0 0]]

#   [[0 0 0 0 0]
#    [0 0 0 0 0]]]]

print(numpy.ones(shape, numpy.int))
# [[[[1 1 1 1 1]
#    [1 1 1 1 1]]

#   [[1 1 1 1 1]
#    [1 1 1 1 1]]]


#  [[[1 1 1 1 1]
#    [1 1 1 1 1]]

#   [[1 1 1 1 1]
#    [1 1 1 1 1]]]


#  [[[1 1 1 1 1]
#    [1 1 1 1 1]]

#   [[1 1 1 1 1]
#    [1 1 1 1 1]]]]


""" Reference

print(numpy.zeros((1, 2)))  # Default type is float
# [[ 0.  0.]]

print(numpy.ones((1, 2), dtype=numpy.int))  # Type changes to int
# [[1 1]]

"""
