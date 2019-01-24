# https://www.hackerrank.com/challenges/np-sum-and-prod/problem


# Inputs
standard_input = """3 3
1 1 1
1 1 1
1 1 1"""

# no-use-before-def
m = None


import numpy


m,n = [int(s) for s in input().split()]
# 3 3

arr = numpy.array([input().split() for _ in range(m)], int)
# 1 1 1
# 1 1 1
# 1 1 1

result = numpy.sum(arr, axis = 0)
# print(result)
# [3 3 3]

result = numpy.prod(result)
print(result)
# 27


""" Reference

my_array = numpy.array([ [1, 2], [3, 4] ])

print (numpy.sum(my_array, axis = 0))
# [4 6]
print (numpy.sum(my_array, axis = 1))
# [3 7]
print (numpy.sum(my_array, axis = None))
# 10
print (numpy.sum(my_array))
# 10

print (numpy.prod(my_array, axis = 0))
# [3 8]
print (numpy.prod(my_array, axis = 1))
# [ 2 12]
print (numpy.prod(my_array, axis = None))
# 24
print (numpy.prod(my_array))
# 24

"""