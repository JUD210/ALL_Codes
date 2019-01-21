# https://www.hackerrank.com/challenges/np-concatenate/problem


standard_input = """4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4
"""
standard_input += """4 3 2
1 2
1 2
1 2
1 2
3 4
3 4
3 4"""


import numpy

""" Solution """
n, m, p = [int(n) for n in input().split()]
# 4 3 2

arrA = numpy.array([input().split() for _ in range(n)], int)
# 1 2  ### n*p
# 1 2
# 1 2
# 1 2
arrB = numpy.array([input().split() for _ in range(m)], int)
# 3 4  ### m*p
# 3 4
# 3 4

# print(arrA)
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]]

# print(arrB)
# [[3 4]
#  [3 4]
#  [3 4]]

print(numpy.concatenate((arrA, arrB)))
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]


""" My Solution not using concatenate (trick) """
n, m, p = [int(n) for n in input().split()]
# 4 3 2

arrays = []
for _ in range(n + m):
    arrays.append(numpy.array([int(numbers) for numbers in input().split()]))
# 1 2  ### n*p
# 1 2
# 1 2
# 1 2
# 3 4  ### m*p
# 3 4
# 3 4


# print(array)
# [array([1, 2]), array([1, 2]), array([1, 2]), array([1, 2]), array([3, 4]), array([3, 4]), array([3, 4])]

print(numpy.array(list(arrays)))
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]]


""" Reference """

# concatenate() takes at most 3 arguments

arrays = []
arrays.append(numpy.array([[1, 2, 3], [4, 5, 6]]))
arrays.append(numpy.array([[7, 8, 9], [10, 11, 12]]))
arrays.append(numpy.array([[13, 14, 15], [16, 17, 18]]))

print(*arrays, sep="\n")
# [[1 2 3]
#  [4 5 6]]
# [[ 7  8  9]
#  [10 11 12]]
# [[13 14 15]
#  [16 17 18]]

print(numpy.concatenate(tuple(arrays)))
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]
#  [16 17 18]]

print(numpy.concatenate(tuple(arrays), axis=1))
# [[ 1  2  3  7  8  9 13 14 15]
#  [ 4  5  6 10 11 12 16 17 18]]
