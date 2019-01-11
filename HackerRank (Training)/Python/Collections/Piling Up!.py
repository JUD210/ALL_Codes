# https://www.hackerrank.com/challenges/piling-up/problem


""" Solution """
from collections import deque

for _ in range(int(input())):
    # 2

    n = int(input())
    dq = deque(map(int, input().split()))
    # 10
    # 8 7 6 5 4 3 2 3
    # 3
    # 1 3 2

    for cube in reversed(sorted(dq)):
        if dq[-1] == cube:
            dq.pop()
        elif dq[0] == cube:
            dq.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")
# Yes
# No

""" My Answer """
""" (WRONG Answer !!!) """
""" I'll not fix it for the remind of mistake. """
# you can only pick up EITHER the leftmost or the rightmost cube each time.
# I understood that can only pick up left, right, left, right, ...

for _ in range(int(input())):
    # 2

    n, *lengths = int(input()), *map(int, input().split())
    # 10
    # 8 7 6 5 4 3 2 3
    # 3
    # 1 3 2

    result = "Yes"

    for i in range(round(n / 2) - 1):
        if lengths[i] < lengths[i + 1] or lengths[n - 1 - i] < lengths[n - 2 - i]:
            result = "No"

    print(result)
    # No (WRONG!)
    # No
