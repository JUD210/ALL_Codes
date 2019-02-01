# https://www.hackerrank.com/challenges/matching-range-of-characters/problem


import re


# Inputs
standard_input = """a4$?ZWe41.l;'a"""


Regex_Pattern = r"^[a-z][1-9][^a-z][^A-Z][A-Z]"  # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
