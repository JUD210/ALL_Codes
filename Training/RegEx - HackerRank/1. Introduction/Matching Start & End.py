# https://www.hackerrank.com/challenges/matching-start-end/problem


import re


# Inputs
standard_input = """0qwer."""


Regex_Pattern = r"^\d\w{4}\.$"  # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
