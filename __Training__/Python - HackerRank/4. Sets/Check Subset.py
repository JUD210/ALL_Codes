# https://www.hackerrank.com/challenges/py-check-subset/problem


for _ in range(int(input())):
# 3
    n1, s1, n2, s2 = [set(map(int, input().split())) for _ in range(4)]
    # 5
    # 1 2 3 5 6
    # 9
    # 9 8 5 6 3 2 1 4 7

    # 1
    # 2
    # 5
    # 3 6 5 4 1

    # 7
    # 1 2 3 5 6 8 9
    # 3
    # 9 8 2
    if s1 & s2 == s1:
        print("True")
    else:
        print("False")

    # True
    # False
    # False

