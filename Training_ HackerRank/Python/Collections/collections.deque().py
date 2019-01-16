# https://www.hackerrank.com/challenges/py-collections-deque/problem


from collections import deque


""" Solution """

d = deque()
for _ in range(int(input())):
    # 4

    method, *args = input().split()
    # append 1
    # append 2
    # append 3
    # appendleft 4
    # pop
    # popleft
    getattr(d, method)(*map(int, args))

print(*d)
# 1 2


""" My Answer """

dq = deque()

dq_methods = {
    "append": dq.append,
    "appendleft": dq.appendleft,
    "pop": dq.pop,
    "popleft": dq.popleft,
}


for _ in range(int(input())):
    # 6

    method, *element = input().split()
    dq_methods[method](*map(int, element))
    # append 1
    # append 2
    # append 3
    # appendleft 4
    # pop
    # popleft

print(*dq)
# 1 2
