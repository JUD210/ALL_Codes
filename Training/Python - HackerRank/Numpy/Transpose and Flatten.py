# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem


import numpy

len_row, len_column = [int(s) for s in input().split()]
# 4 3

arr = []
for _ in range(len_row):
    arr.append([int(s) for s in input().split()])
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

arr = numpy.array(arr)
# print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

print(arr.transpose())
# [[ 1  5  9 13]
#  [ 2  6 10 14]
#  [ 3  7 11 15]
#  [ 4  8 12 16]]

print(arr.flatten())
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16]

# print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
