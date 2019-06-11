# https://www.hackerrank.com/challenges/matrix-script/problem


import re

m, n = [int(num) for num in input().split()]
# 7 3

matrix = []
for _ in range(m):
    matrix.append(input())
    # Tsi
    # h%x
    # i #
    # sM
    # $a
    # #t%
    # ir!

s = "".join(["".join(tpl) for tpl in zip(*matrix)])
# This$#is% Matrix#  %!

print(re.sub(r"(?<=\w)[!@#$%^ ]+(?=\w)"," ", s))
# This is Matrix#  %!
