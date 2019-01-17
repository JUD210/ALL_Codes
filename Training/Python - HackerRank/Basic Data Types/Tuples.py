# https://www.hackerrank.com/challenges/python-tuples/problem


num = int(input())
# 2
int_list = tuple(map(int, input().split()))
# 1 2

print(hash(int_list))
# 3713081631934410656