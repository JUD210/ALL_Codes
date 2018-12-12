# https://www.hackerrank.com/challenges/nested-list/problem


n = int(input())
# 5

names = set()
scores = set()
students = []

for i in range(n):
    t_name = input()
    t_score = float(input())
    # Harry
    # 37.21
    # Berry
    # 37.21
    # Tina
    # 37.2
    # Akriti
    # 41
    # Harsh
    # 39

    names.add(t_name)
    scores.add(t_score)
    students.append([t_name, t_score])

scores.remove(min(scores))

result_name = []
for name, score in students:
    if score == min(scores):
        result_name.append(name)

result_name.sort()
print(*result_name, sep="\n")
# Berry
# Harry
