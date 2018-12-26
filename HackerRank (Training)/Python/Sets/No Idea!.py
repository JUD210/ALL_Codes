# https://www.hackerrank.com/challenges/no-idea/problem


n, m = input().split()
# 3 2
# 3   # len(arr)
# 2   # len(set)

arr = [int(x) for x in input().split()]
# 1 5 3
A = set([int(y) for y in input().split()])
# 3 1
B = set([int(z) for z in input().split()])
# 5 7

count = sum([1 if x in A else -1 if x in B else 0 for x in arr])
print(count)
# 1
