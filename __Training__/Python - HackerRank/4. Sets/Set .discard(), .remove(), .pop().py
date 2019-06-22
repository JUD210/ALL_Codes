# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


n = int(input())
# 9

s = set(map(int, input().split()))
# 1 2 3 4 5 6 7 8 9

methods = {"pop": s.pop, "remove": s.remove, "discard": s.discard}

for _ in range(int(input())):
    # 5
    method, *args = input().split()

    if len(args) > 1:
        for arg in args:
            methods[method](*map(int, arg))

        """ I used below code, and it's not good.

        [methods[method](*map(int, arg)) for arg in args]

        for a sequence of actions: Loop
        for a sequence of values: List or generator comprehension
        """
    else:
        methods[method](*map(int, args))

# pop
# {2, 3, 4, 5, 6, 7, 8, 9}
# pop
# {3, 4, 5, 6, 7, 8, 9}
# discard 1 2 3
# {4, 5, 6, 7, 8, 9}
# remove 5 7 9
# {4, 6, 8}
# pop
# {6, 8}

print(sum(s))
# 14
