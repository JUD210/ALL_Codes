# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


s1, s2 = [set(input().split()) for _ in range(4)][1::2]
# 9   # len(s1)
# 1 2 3 4 5 6 7 8 9
# 9   # len(s2)
# 10 1 2 3 11 21 55 6 8

# A n B
print(len(s1 & s2))
# print(len(s1.intersection(s2)))
# 5