# https://www.hackerrank.com/challenges/np-arrays/problem


import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1], float)


arr = input().strip().split(" ")
# 1 2 3 4 -8 -10
result = arrays(arr)
print(result)
# [-10.  -8.   4.   3.   2.   1.]
