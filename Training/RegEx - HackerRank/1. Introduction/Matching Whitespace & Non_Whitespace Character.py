# https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem


import re

# Inputs
standard_input = """12 11 15"""


Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
