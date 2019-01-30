# https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem


import re


# Inputs
standard_input = """06-11-2015"""


Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
