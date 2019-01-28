"""

When I was searching about,

List Comprehension
vs
Map & Lambda

I realized there are many discussions like below link.

# https://stackoverflow.com/questions/1247486/list-comprehension-vs-map


They compare performances in terms of speed, memory,
and readability in terms of pythonic, elegance.


That made me think about priority, and this is the conclusion.


~ My Priority

0. Safety & Compatibility
1. Performance
2. Readbility

"""



""" Comapre below 2 """
len_students, len_subjects = [int(s) for s in input().split()]

len_students, len_subjects = map(int, input().split())
""""""
# 5 3

subjects = []
for _ in range(len_subjects):
    subjects.append(list(map(float, input().split())))
    # 89 90 78 93 80
    # 90 91 85 88 86
    # 91 92 83 89 90.5

""" Comapre below 3 """
for student in zip(*subjects):
    print(sum(student) / len(student))

print(*map(lambda s: sum(s) / len(s), zip(*subjects)), sep="\n")

print(*[sum(s) / len(s) for s in zip(*subjects)], sep="\n")
""""""
# 90.0
# 91.0
# 82.0
# 90.0
# 85.5
