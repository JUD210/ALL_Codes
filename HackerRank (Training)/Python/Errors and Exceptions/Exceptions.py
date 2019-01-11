# https://www.hackerrank.com/challenges/exceptions/problem


for _ in range(int(input())):
    # 3

    try:
        a, b = map(int, input().split())
        # 1 0
        # 2 $
        # 3 1
        print(int(a) // int(b))

    except Exception as e:
        print("Error Code:", e)

# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3
