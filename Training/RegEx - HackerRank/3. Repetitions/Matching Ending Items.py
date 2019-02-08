# https://www.hackerrank.com/challenges/matching-ending-items/problem


import re


# Inputs
standard_input = """1less"""


Regex_Pattern = r"^[a-zA-Z]*s$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
