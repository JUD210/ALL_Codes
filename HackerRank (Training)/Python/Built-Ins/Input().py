# https://www.hackerrank.com/challenges/input/problem


x, k = map(int, input().split())
# 1 4

polynomial = input()
print(eval(polynomial) == k)
# x**3 + 2x**2 + 3x + 4
# True
