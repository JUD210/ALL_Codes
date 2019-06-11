# https://www.hackerrank.com/challenges/30-sorting/problem


# Inputs
standard_input = """3
3 2 1"""


num = int(input())
# 3

l = [int(s) for s in input().split()]
# 3 2 1

swap_count = 0
for i in range(num):
    for j in range(num - i - 1):
        if l[j] > l[j + 1]:
            tmp = l[j]
            l[j] = l[j + 1]
            l[j + 1] = tmp
            swap_count += 1

print(f"Array is sorted in {swap_count} swaps.")
print(f"First Element: {l[0]}")
print(f"Last Element: {l[-1]}")
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3
