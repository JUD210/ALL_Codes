# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


import re


# Inputs
standard_input = """14"""


Regex_Pattern = r"^\d{2,}[a-z]*[A-Z]*$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
