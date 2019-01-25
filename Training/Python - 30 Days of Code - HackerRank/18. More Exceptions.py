# https://www.hackerrank.com/challenges/30-more-exceptions/problem


# Inputs
standard_input = """4
3 5
2 4
-1 -2
-1 3"""

# Write your code here
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n ** p


myCalculator = Calculator()

T = int(input())
# 4

for i in range(T):
    n, p = map(int, input().split())
    # 3 5
    # 2 4
    # -1 -2
    # -1 3

    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

# 243
# 16
# n and p should be non-negative
# n and p should be non-negative
