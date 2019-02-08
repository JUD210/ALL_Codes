# https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem


import re

# Inputs
standard_input = """3threeormorealphabets."""


Regex_Pattern = r"^\d{1,2}[a-zA-Z]{3,}\.{0,3}$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
