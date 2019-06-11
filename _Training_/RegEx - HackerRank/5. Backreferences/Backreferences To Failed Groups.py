# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem


import re


# Inputs
standard_input = """12-34-56-78"""


Regex_Pattern = r"^\d{2}(-?)(?:\d{2}\1){2}\d{2}$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
