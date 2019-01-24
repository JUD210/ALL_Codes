# https://www.hackerrank.com/challenges/np-linear-algebra/problem


# Inputs
standard_input = """2
1.1 1.1
1.1 1.1"""


import numpy


n = int(input())
# 2

a = numpy.array([input().split() for _ in range(n)], float)
# 1.1 1.1
# 1.1 1.1

numpy.set_printoptions(legacy="1.13")
print(numpy.linalg.det(a))
# 0.0


""" Reference 

[linalg.det]

The linalg.det tool computes the determinant of an array.

print(numpy.linalg.det([[1, 2], [2, 1]]))
# -3.0


[linalg.eig]

The linalg.eig computes the eigenvalues and right eigenvectors of a square array.

vals, vecs = numpy.linalg.eig([[1, 2], [2, 1]])

print(vals)
# [ 3. -1.]
print(vecs)
# [[ 0.70710678 -0.70710678]
#  [ 0.70710678  0.70710678]]


[linalg.inv]

The linalg.inv tool computes the (multiplicative) inverse of a matrix.

print(numpy.linalg.inv([[1, 2], [2, 1]]))
# [[-0.33333333  0.66666667]
#  [ 0.66666667 -0.33333333]]

"""
