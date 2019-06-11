# https://www.hackerrank.com/challenges/matching-same-text-again-again/problem


import re


# Inputs
standard_input = """ab #1?AZa$ab #1?AZa$"""


Regex_Pattern = r"^([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S)\1$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
