# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem


# Inputs
standard_input = """za"""


s = input()
# za

try:
    print(int(s))
except ValueError:
    print("Bad String")
# Bad String
