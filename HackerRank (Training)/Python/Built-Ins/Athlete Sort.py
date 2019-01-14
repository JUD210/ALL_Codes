# https://www.hackerrank.com/challenges/python-sort-sort/problem


len_row, len_column = [int(s) for s in input().split()]
# 5 3

sheet = []
for _ in range(len_row):
    sheet.append([int(s) for s in input().split()])
    # 10 2 5
    # 7 1 0
    # 9 9 9
    # 1 23 12
    # 6 5 9

finder = int(input())
# 1

for row in sorted(sheet, key=lambda s: s[finder]):
    print(*row)

# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
