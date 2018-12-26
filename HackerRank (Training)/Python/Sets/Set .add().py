# https://www.hackerrank.com/challenges/py-set-add/problem


n = int(input())
# 7   # len(set)

s = set()
for _ in range(n):
    s.add(input())
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

print(len(s))
# 5