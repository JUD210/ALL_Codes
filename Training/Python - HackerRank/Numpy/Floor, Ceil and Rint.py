# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem


# Inputs
standard_input = """1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"""


import numpy


arr = numpy.array(input().split(), dtype=float)

numpy.set_printoptions(legacy="1.13")
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

""" Using RegEx
# import re
# print(re.sub(r"(\d*\.\d*)", r" \1", str(numpy.floor(arr))))
# print(re.sub(r"(\d*\.\d*)", r" \1", str(numpy.ceil(arr))))
# print(re.sub(r"(\d*\.\d*)", r" \1", str(numpy.rint(arr))))
"""

# from

# [1. 2. 3. 4. 5. 6. 7. 8. 9.]
# [ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
# [ 1.  2.  3.  4.  6.  7.  8.  9. 10.]

# to

# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]


""" Reference

arr = numpy.array([-2.2, -1.1, 0, 1.1, 2.2])

print(numpy.floor(arr))
# [-3. -2.  0.  1.  2.]

print(numpy.ceil(arr))
# [-2. -1.  0.  2.  3.]

print(numpy.rint(arr))
# [-2. -1.  0.  1.  2.]

"""
