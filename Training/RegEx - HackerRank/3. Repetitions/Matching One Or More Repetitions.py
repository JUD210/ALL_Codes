# https://www.hackerrank.com/challenges/matching-one-or-more-repititions/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re


# Inputs
standard_input = """1Qa"""


Regex_Pattern = r"^\d+[A-Z]+[a-z]+$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
