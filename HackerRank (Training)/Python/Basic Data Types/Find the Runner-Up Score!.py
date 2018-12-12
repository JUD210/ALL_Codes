# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem


n = int(input())
arr = sorted(list(set((map(int, input().rstrip().split())))))
# 6
# 1 2 6 7 6 45 43 6 7 5 4 4 5 6 100

print(arr[-2])
# 100