# https://www.hackerrank.com/challenges/any-or-all/problem


len_numbers, numbers = input(), input().split()
# 6
# 1 2 11 121 -9
print(all([int(n) > 0 for n in numbers]) and any([n == n[::-1] for n in numbers]))
# False
