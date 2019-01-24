# https://www.hackerrank.com/challenges/np-eye-and-identity/problem


# Inputs
standard_input = """3 3"""


import numpy


shape = [int(s) for s in input().split()]

numpy.set_printoptions(legacy="1.13")
print(numpy.eye(*shape))

""" Using RegEx
import re
print(re.sub(r"(\d\.)", r" \1", str(numpy.eye(*shape))))
"""

# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]


""" Reference

print(numpy.identity(3))
# 3 is for  dimension 3 X 3

# Output
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

print(numpy.eye(5, 4, k=1))
# 5 X 4 Dimensional array with first upper diagonal 1.

# [[0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print(numpy.eye(5, 4, k=-2))
# 5 X 4 Dimensional array with second lower diagonal 1.

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]]

"""
