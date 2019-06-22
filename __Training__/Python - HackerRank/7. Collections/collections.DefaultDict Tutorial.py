# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


from collections import defaultdict

"""
d = defaultdict(list)

d["python"].append("awesome")
# [].append("awesome")

d["python"].append("language")
# ["awesome"].append("language")

d["something-else"]
# []


print(d, sep="\n")
# defaultdict(<class 'list'>, {'python': ['awesome', 'language'], 'something-else': []})

print(dict(d), sep="\n")
# {'python': ['awesome', 'language'], 'something-else': []}

print(*[i for i in d.items()], sep="\n")
# ('python', ['awesome', 'language'])
# ('something-else', [])

"""

len_dic, len_sel = map(int, input().split())
# 5 3

d = defaultdict(list)

for i in range(len_dic):
    d[input()].append(i + 1)
# a
# a
# b
# a
# b

for sel in [input() for _ in range(len_sel)]:
    # a
    # b
    # z

    print(*d[sel]) if sel in d.keys() else print(-1)
    # 1 2 4
    # 3 5
    # -1
