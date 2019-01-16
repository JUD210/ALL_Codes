# https://www.hackerrank.com/challenges/py-set-mutations/problem


s = [set(map(int, input().split())) for _ in range(2)][1]
# 16   # len(s)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52


methods1 = {
    "update": s.update,
    "difference_update": s.difference_update,
    "intersection_update": s.intersection_update,
    "symmetric_difference_update": s.symmetric_difference_update
}

def methods2(m, s, sub_s):
    if m == "update":
        s |= sub_s
    elif m == "difference_update":
        s -= sub_s
    elif m == "intersection_update":
        s &= sub_s
    elif m == "symmetric_difference_update":
        s ^= sub_s
    
for _ in range(int(input())):
# 4
    m, sub_s = input().split()[0], set(map(int, input().split()))
    # intersection_update 10
    # 2 3 5 6 8 9 1 4 7 11
    # update 2
    # 55 66
    # symmetric_difference_update 5
    # 22 7 35 62 58
    # difference_update 7
    # 11 22 35 55 58 62 66

    methods1[m](sub_s)
    # methods2(m, s, sub_s)

print(sum(s))
# 38
