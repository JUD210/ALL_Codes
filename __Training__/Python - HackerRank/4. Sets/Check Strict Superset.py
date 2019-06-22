# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


super_set = set(map(int, input().split()))
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78


result = True
for _ in range(int(input())):
# 2
    sub_set = set(map(int, input().split()))
    # 1 2 3 4 5
    # 100 11 12

    if sub_set & super_set != sub_set:
        result = False

print(result)
# False