# https://www.hackerrank.com/challenges/np-arrays/problem


import numpy


def reversed_array(arr):
    return numpy.array(arr[::-1], float)
    # return numpy.flipud(numpy.array(arr,float))


arr = input().strip().split(" ")
# 1 2 3 4 -8 -10

print(reversed_array(arr))
# [-10.  -8.   4.   3.   2.   1.]


""" Reference """

arrA = numpy.array([1, 2, 3], int)
print(arrA)
# [1 2 3]

arrB = numpy.array([[1, 2, 3], [4, 5, 6]], float)
print(arrB)
# [[1. 2. 3.]
#  [4. 5. 6.]]

arr_list = []
arr_list.append(arrA)
arr_list.append(arrB)
print(arr_list)
# [array([1, 2, 3]), array([[1., 2., 3.],
#        [4., 5., 6.]])]
