# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem


# Inputs
standard_input = """2 2
1 2
3 4"""

# no [use-before-def]
m = None


import numpy


m, n = [int(s) for s in input().split()]
# 2 2

arr = numpy.array([input().split() for _ in range(m)], int)
# 1 2
# 3 4

numpy.set_printoptions(legacy="1.13")

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr, axis=None))
# [ 1.5  3.5]
# [ 1.  1.]
# 1.11803398875


""" Reference

my_array = numpy.array([[1, 2], [3, 4]])

print(numpy.mean(my_array, axis=0))
# [2. 3.]
print(numpy.mean(my_array, axis=1))
# [1.5 3.5]
print(numpy.mean(my_array, axis=None))
# 2.5
print(numpy.mean(my_array))
# 2.5


print(numpy.var(my_array, axis=0))
# [1. 1.]
print(numpy.var(my_array, axis=1))
# [0.25 0.25]
print(numpy.var(my_array, axis=None))
# 1.25
print(numpy.var(my_array))
# 1.25

print(numpy.std(my_array, axis=0))
# [1. 1.]
print(numpy.std(my_array, axis=1))
# [0.5 0.5]
print(numpy.std(my_array, axis=None))
# 1.11803398875
print(numpy.std(my_array))
# 1.11803398875

"""
