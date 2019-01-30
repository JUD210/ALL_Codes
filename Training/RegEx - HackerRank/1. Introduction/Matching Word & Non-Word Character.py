# https://www.hackerrank.com/challenges/matching-word-non-word/problem?h_r=next-challenge&h_v=zen


import re


# Inputs
standard_input = """www.hackerrank.com"""


Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
