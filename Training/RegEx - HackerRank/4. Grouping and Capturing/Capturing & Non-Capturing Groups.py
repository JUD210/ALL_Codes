# https://www.hackerrank.com/challenges/capturing-non-capturing-groups/problem


import re


# Inputs
standard_input = """okokok! cya"""


Regex_Pattern = r"(ok)\1\1"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
