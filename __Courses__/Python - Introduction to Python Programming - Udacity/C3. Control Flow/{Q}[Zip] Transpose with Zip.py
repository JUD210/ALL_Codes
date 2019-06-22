"""
Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.
"""

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
# 0  1  2
# 3  4  5
# 6  7  8
# 9  10 11
#
# Transpose : [data]^T
#
# 0  3  6  9
# 1  4  7  10
# 2  5  8  11

data_transpose = tuple(zip(*data))
print(data)
print(data_transpose)
