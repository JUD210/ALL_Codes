# https://www.hackerrank.com/challenges/py-the-captains-room/problem


""" Answer """
k, arr = int(input()), list(map(int, input().split()))
# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

myset = set(arr)

print(((sum(myset) * k) - (sum(arr))) // (k - 1))
# 8
# 29*5(=145) - 113 // 4

""" Terminated due to timeout :(

k = int(input())
# 5

num_list = list(map(int, input().split()))
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

num_set = set(num_list)


result = 0
for num in num_set:
    if(num_list.count(num)==1):
        result = num

print(result)
# 8
"""
