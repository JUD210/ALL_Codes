# https://www.hackerrank.com/challenges/np-array-mathematics/problem


# Inputs
standard_input = """2 4
1 2 3 4
1 2 3 4
5 6 7 7
5 6 7 7"""

# no [use-before-def]
m = None


import numpy


m, n = [int(s) for s in input().split()]
# 2 4

a = numpy.array([input().split() for _ in range(m)], int)
# 1 2 3 4
# 1 2 3 4

b = numpy.array([input().split() for _ in range(m)], int)
# 5 6 7 7
# 5 6 7 7

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
# [[ 6  8 10 11]
#  [ 6  8 10 11]]
# [[-4 -4 -4 -3]
#  [-4 -4 -4 -3]]
# [[ 5 12 21 28]
#  [ 5 12 21 28]]
# [[0 0 0 0]
#  [0 0 0 0]]
# [[1 2 3 4]
#  [1 2 3 4]]
# [[    1    64  2187 16384]
#  [    1    64  2187 16384]]


""" Reference

a = numpy.array([1, 2, 3, 4], float)
b = numpy.array([5, 6, 7, 8], float)

print(a + b)
print(numpy.add(a, b))
# [ 6.  8. 10. 12.]
# [ 6.  8. 10. 12.]

print(a - b)
print(numpy.subtract(a, b))
# [-4. -4. -4. -4.]
# [-4. -4. -4. -4.]

print(a * b)
print(numpy.multiply(a, b))
# [ 5. 12. 21. 32.]
# [ 5. 12. 21. 32.]

print(a / b)
print(numpy.divide(a, b))
# [0.2        0.33333333 0.42857143 0.5       ]
# [0.2        0.33333333 0.42857143 0.5       ]

print(a % b)
print(numpy.mod(a, b))
# [1. 2. 3. 4.]
# [1. 2. 3. 4.]

print(a ** b)
print(numpy.power(a, b))
# [1.0000e+00 6.4000e+01 2.1870e+03 6.5536e+04]
# [1.0000e+00 6.4000e+01 2.1870e+03 6.5536e+04]

"""
