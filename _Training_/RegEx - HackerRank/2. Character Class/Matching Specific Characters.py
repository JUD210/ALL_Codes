# https://www.hackerrank.com/challenges/matching-specific-characters/problem


import re


# Inputs
standard_input = """1203x."""


Regex_Pattern = r"^[123][120][xs0][30Aa][xsu][.,]$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
