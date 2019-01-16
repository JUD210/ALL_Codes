# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem


import numpy

len_row, len_column = [int(s) for s in input().split()]
# 3 3

arr = []
for _ in range(len_row):
    arr.append([int(s) for s in input().split()])
# 1 2 3
# 4 5 6
# 7 8 9

arr = numpy.array(arr)
# print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(arr.transpose())
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

print(arr.flatten())
# [1 2 3 4 5 6 7 8 9]
