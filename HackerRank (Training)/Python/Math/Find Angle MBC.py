# https://www.hackerrank.com/challenges/find-angle/problem


import math

seg_ab, seg_bc = int(input()), int(input())
# 3
# 7

print(str(int(round((math.degrees(math.atan2(seg_ab, seg_bc)))))) + "°")
# 23°
