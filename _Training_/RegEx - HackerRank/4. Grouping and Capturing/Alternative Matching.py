# https://www.hackerrank.com/challenges/alternative-matching/problem


import re


# Inputs
standard_input = """Mr.DOSHI"""


Regex_Pattern = r"^(?:Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
