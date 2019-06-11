# https://www.hackerrank.com/challenges/polar-coordinates/problem


import cmath

c_num = input()
# 1+2j

print(*cmath.polar(complex(c_num)), sep="\n")
# 2.23606797749979
# 1.1071487177940904
