# https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem


import re


# Inputs
standard_input = """123.456.abc.def"""


regex_pattern = r".{3}\..{3}\..{3}\..{3}$"  # Do not delete 'r'.


test_string = input()
# 123.456.abc.def

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
# true
