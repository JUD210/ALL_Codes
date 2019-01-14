# https://www.hackerrank.com/challenges/zipped/problem


len_students, len_subjects = [int(s) for s in input().split()]
# len_students, len_subjects = map(int, input().split())
# 5 3

subjects = []
for _ in range(len_subjects):
    subjects.append(list(map(float, input().split())))
    # 89 90 78 93 80
    # 90 91 85 88 86
    # 91 92 83 89 90.5

for student in zip(*subjects):
    print(sum(student) / len(student))
# print(*map(lambda s: sum(s) / len(s), zip(*subjects)), sep="\n")
# print(*[sum(s) / len(s) for s in zip(*subjects)], sep="\n")

# 90.0
# 91.0
# 82.0
# 90.0
# 85.5
